# review/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('give-review/', views.give_review, name='give_review'),
    path('thank-you/', views.thank_you_review, name='thank_you_review'),
    path('all-reviews/', views.all_reviews, name='all_reviews'),
]
