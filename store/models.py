from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models import Count, Sum
from core.models import User
from datetime import datetime 
from django.core.exceptions import ValidationError

from .managers import CommentQuerySet


from apps.catalogue.models import Category, Product

class Store(models.Model):
    LOCATION_CHOICES =[('BW', 'Bweyale'), ('KY', 'Kyradongo')]
  
    name = models.CharField(max_length=15)
    owner = models.OneToOneField(User, related_name="shop", on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    product_type  = models.ManyToManyField(Category)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField()
    date_created = models.DateField('Date created', auto_now_add=True)
    date_modified = models.DateTimeField('Date modified', auto_now=True)
    primary_image = models.ImageField(upload_to='store')
    location_image1 = models.ImageField(upload_to='location', default='image_not_found.jpg')
    location_image2 = models.ImageField(upload_to='location', default='image_not_found.jpg')
    location_image3 = models.ImageField(upload_to='location', default='image_not_found.jpg')
    location_image4 = models.ImageField(upload_to='location', default='image_not_found.jpg')

    def __str__(self):
        return self.name
    
    def get_slug(self):
        return slugify(self.name)


    def get_absolute_url(self):
        """
            Get the store 
        """
        return reverse('store:store', kwargs={'pk': self.pk , 'slug':self.slug})

    
    def update_rating(self):
        """
        Recalculate rating field
        """
        self.record.rating = self.calculate_rating()
        self.record.save()

    update_rating.alters_data = True

    def calculate_rating(self):
        """
        Calculate rating value
        """
        result = self.comments.filter(type='PC').aggregate(
            sum=Sum("score"), count=Count("id")
        )
        reviews_sum = result["sum"] or 0
        reviews_count = result["count"] or 0
        rating = None
        if reviews_count > 0:
            rating = float(reviews_sum) / reviews_count
        return rating

class StoreRecord(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE ,  related_name='record')
    views = models.IntegerField(default=0)
    # Ratings are between 0 and 5
    RATING_CHOICES = tuple([(x, x) for x in range(0, 6)])
    rating = models.PositiveSmallIntegerField( "Rating", choices=RATING_CHOICES, default=0)
    products = models.ManyToManyField(Product, related_name='store_record', blank=True)
    staff = models.ManyToManyField(User, related_name='stores')
    store_followers = models.ManyToManyField(User, through='FollowInfo')

    def __str__(self):
        return self.store.name
    
class FollowInfo(models.Model):
    follower_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_store')
    store_record = models.ForeignKey(StoreRecord, on_delete=models.CASCADE)
    date_followed = models.DateTimeField(auto_now_add=True)

class UserStoreRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    no_of_views = models.PositiveBigIntegerField()
    date_viewed = models.DateTimeField(auto_now_add=True)
    last_viewed = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    TYPE_CHOICES = [
        ('PC', 'Parent Comment'),
        ('R', 'Reply')
    ]
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    message = models.TextField('Body')
    type = models.CharField(max_length=16, choices=TYPE_CHOICES, default='PC')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    total_votes = models.IntegerField('Total votes', default=0)
    delta_votes = models.IntegerField('Delta Votes', default=0)
    
    date_created = models.DateField('Date created', auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='comments')
    # Scores are between 0 and 5
    SCORE_CHOICES = tuple([(x, x) for x in range(0, 6)])
    score = models.PositiveSmallIntegerField( "Score", choices=SCORE_CHOICES)

    objects = CommentQuerySet.as_manager()


    class Meta:
        ordering = ["-delta_votes", "id"]

    def __str__(self):
        return self.title
    
    def vote_up(self, user):
        self.votes.create(user=user, delta=Vote.UP)

    def vote_down(self, user):
        self.votes.create(user=user, delta=Vote.DOWN)

    def can_user_vote(self, user):
        """
        Test whether the passed user is allowed to vote on this
        review
        """
        if not user.is_authenticated:
            return False, _("Only signed in users can vote")
        # pylint: disable=no-member
        vote = self.votes.model(comment=self, user=user, delta=1)
        try:
            vote.full_clean()
        except ValidationError as e:
            return False, "%s" % e
        return True, ""
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.store.update_rating()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        if self.store is not None:
            self.store.update_rating()

    
    def update_totals(self):
        """
        Update total and delta votes
        """
        result = self.votes.aggregate(score=Sum("delta"), total_votes=Count("id"))
        self.total_votes = result["total_votes"] or 0
        self.delta_votes = result["score"] or 0
        self.save()

    @property
    def is_anonymous(self):
        return self.user is None
    
    @property
    def has_votes(self):
        return self.total_votes > 0

    @property
    def num_up_votes(self):
        """Returns the total up votes"""
        return int((self.total_votes + self.delta_votes) / 2)

    @property
    def num_down_votes(self):
        """Returns the total down votes"""
        return int((self.total_votes - self.delta_votes) / 2)
    
    @property
    def has_replies(self):
        """Return true if comment has replies"""
        return self.replies.filter().exists()
    @property
    def is_parent(self):
        """Returns true is comment is a parent comment"""
        if self.type == 'PC':
            return True
        else:
            return False
    

class Vote(models.Model):
    """
    Records user comment as yes/no vote.

    * Only signed-in users can vote.
    * Each user can vote only once.
    """

    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="votes"
    )
    user = models.ForeignKey(
        User, related_name="comment_votes", on_delete=models.CASCADE
    )
    UP, DOWN = 1, -1
    VOTE_CHOICES = ((UP, "Up"), (DOWN, "Down"))
    delta = models.SmallIntegerField("Delta", choices=VOTE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]
        verbose_name = "Comment Vote"
        verbose_name_plural = "Comment Votes"

    def __str__(self):
        return "%s vote for %s" % (self.delta, self.comment)
    
    def clean(self):
        if not self.comment.is_anonymous and self.comment.user == self.user:
            raise ValidationError("You cannot vote on your own comment")
        if not self.user.id:
            raise ValidationError("Only signed-in users can vote on comments")
        previous_votes = self.comment.votes.filter(user=self.user)
        if len(previous_votes) > 0:
            print(previous_votes)
            previous_votes.delete()
            # raise ValidationError("You can only vote once on a review")



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.comment.update_totals()



    
