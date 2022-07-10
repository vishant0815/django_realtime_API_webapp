from django.urls import path
from Internship import views

urlpatterns = [
    path('', views.index, name='indexfile'),
    path('aboutus', views.aboutus, name='aboutusfile'),
    path('404', views.page, name='404file'),
    path('world', views.world, name='worldfile'),
    path('startup', views.startup, name='startupfile'),
    path('technology', views.technology, name='technologyfile'),
    path('business', views.business, name='businessfile'),
    path('sports', views.sports, name='sportsfile'),
    path('entertainment', views.entertainment, name='entertainmentfile'),
    path('politics', views.politics, name='politicsfile'),
    path('automobile', views.automobile, name='automobilefile'),
    path('travel', views.travel, name='travelfile'),
    path('contactus', views.contactus, name='contactusfile'),
]