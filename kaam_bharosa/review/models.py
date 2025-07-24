# review/models.py

from django.db import models
from django.contrib.auth.models import User

class AppReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('Job Dene Wale', 'Job Dene Wale'), ('Job Lene Wale', 'Job Lene Wale')])
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}"
