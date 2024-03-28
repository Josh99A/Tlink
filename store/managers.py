from django.db import models

class CommentQuerySet(models.QuerySet):
    def only_parent_comments(self):
        return self.filter(type='PC')