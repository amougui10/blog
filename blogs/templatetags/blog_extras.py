from django import template
from django.utils import timezone

# MINUTE = 60
# HOUR = 60 * MINUTE
# DAY = 24 * HOUR

# register = template.Library()


# @register.filter
# def model_type(value):
#     return type(value).__name__


# @register.filter
# def get_posted_at_display(posted_at):
#     seconds_ago = (timezone.now() - posted_at).total_seconds()
#     if seconds_ago <= HOUR:
#         return f'Publié il y a {int(seconds_ago // MINUTE)} minutes.'
#     elif seconds_ago <= DAY:
#         return f'Publié il y a {int(seconds_ago // HOUR)} heures.'
#     return f'Publié le {posted_at.strftime("%d %b %y à %Hh%M")}'


# @register.simple_tag(takes_context=True)
# def get_poster_display(context, user):
#     if user == context['user']:
#         return 'vous'
#     return user.username

MINUTE  = 60
HOUR = 60 * MINUTE
DAY  = 24 * HOUR

register = template.Library()

@register.filter
def model_type(value):
    
    return type(value).__name__

@register.filter
def  get_posted_at_display(posted_at):
    
    seconds_ago =(timezone.now()-posted_at).total_seconds()
    
    if seconds_ago<=HOUR:
        
        return f' Publier il ya {int(seconds_ago//MINUTE)}minutes.'
    
    elif seconds_ago<= DAY:
        return f' Publier le {posted_at.strftime("%d %b %y a %Hh%M")}heures.'
    
@register.simple_tag(takes_context = True)
def get_poster_display(context, user):
        if user == context['user']:
            return 'Vous'
        return user.username







# <!-- <h2>Votre flux</h2>
# <div class="grid-container">
#     {% for instance in blogs_and_photos %}
#         {% if instance|model_type == 'Blog' %}
#     <div class="post">
#         <a href="{% url 'view.blog' instance.id %}"> 
#         <h4>Billet : {{instance.title}}</h4>
#         <img src="{{instance.photo.image.url}}">
#         <p><strong>Ecrit par {{instance.contributors.all|join:" ," }}</strong></p>
#         <p>{{instance.date_created|get_posted_at_display}}</p>
#         </a>
#     </div>
#     {% elif instance | model_type =='Photo' %}
#     <div class="post">
#         <img src ="{{instance.image.url }}">
#         <p>{{instance.caption}}</p>
#         <p><strong>Prise par {% get_poster_display instance.uploader %}</strong></p>
#         <p>{{ instance.date.created | get_posted_at_display  }}</p>
#     </div>
#     {% endif %}
#     {% endfor %}
# </div>

# {% endblock content %}



#     <!-- <h2>Votre flux</h2>
#     <div class="grid-container">
#         {% for instance in blogs_and_photos %}
#             {% if instance|model_type == 'Blog' %}
#                 <div class="post">
#                     <a href="{% url 'view_blog' instance.id %}">
#                         <h4>Billet : {{ instance.title }}</h4>
#                         <img src="{{ instance.photo.image.url }}">
#                         <p><strong>Écrit par {{ instance.contributors.all|join:", " }}</strong></p>
#                         <p>{{ instance.date_created|get_posted_at_display }}</p>
#                     </a>
#                 </div>
#             {% elif instance|model_type == 'Photo' %}
#                 <div class="post">
#                     <img src="{{ instance.image.url }}">
#                     <p>{{ instance.caption }}</p>
#                     <p><strong>Prise par {% get_poster_display instance.uploader %}</strong></p>
#                     <p>{{ instance.date_created|get_posted_at_display }}</p>
#                 </div>
#             {% endif %}
#         {% endfor %}
#     </div>
# {% endblock content %} --> --> 