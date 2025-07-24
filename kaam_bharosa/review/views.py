# review/views.py

from django.shortcuts import render, redirect
from .forms import AppReviewForm
from .models import AppReview
from django.contrib.auth.decorators import login_required

@login_required
def give_review(request):
    if request.method == 'POST':
        form = AppReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('thank_you_review')
    else:
        form = AppReviewForm()
    return render(request, 'reviews/give_review.html', {'form': form})

def thank_you_review(request):
    return render(request, 'reviews/thank_you.html')

def all_reviews(request):
    reviews = AppReview.objects.all().order_by('-created_at')
    return render(request, 'reviews/all_reviews.html', {'reviews': reviews})
