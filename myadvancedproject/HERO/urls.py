from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('blog/', views.blog_view, name='blog'),
    path('team/', views.team_view, name='team'),
    path('testimonials/', views.testimonials_view, name='testimonials'),
]
