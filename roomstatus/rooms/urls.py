from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
]
# because of the name parameter, which uniquely identifies this particular URL mapping, we can now link to this home page from any other page by creating the following link in a template:
# <a href="{% url 'index' %}">Home</a>
