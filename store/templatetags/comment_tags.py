from django import template

register = template.Library()



@register.filter
def may_vote(comment, user):
    can_vote, __ = comment.can_user_vote(user)
    return can_vote

@register.filter
def has_up_vote(comment, user):
    return comment.votes.filter(user=user, delta=1).exists()

@register.filter
def has_down_vote(comment, user):
    return comment.votes.filter(user=user, delta=-1).exists()


