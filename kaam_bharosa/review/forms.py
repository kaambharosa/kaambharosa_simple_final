# review/forms.py

from django import forms
from .models import AppReview

class AppReviewForm(forms.ModelForm):
    class Meta:
        model = AppReview
        fields = ['role', 'rating', 'review_text']
