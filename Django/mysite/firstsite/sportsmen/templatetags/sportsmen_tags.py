from django import template
from sportsmen.models import *

register = template.Library()

@register.simple_tag(name='getsports')
def get_sports():
    return Sports.objects.all()

@register.inclusion_tag('sportsmen/list_sports.html')
def show_sports(sort=None, sport_selected=0):
    if not sort:
        sports = Sports.objects.all()
    else:
        sports = Sports.objects.order_by(sort)
    return {'sports': sports, 'sport_selected': sport_selected}