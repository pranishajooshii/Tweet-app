from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    # Define tweet types (choices) inside the class
    TWEET_CHOICES = [
        ('education', 'Education'),
        ('technology', 'Technology'),
        ('health', 'Health'),
        # Add more types as needed
    ]

    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    type = models.CharField(
        max_length=50, choices=TWEET_CHOICES, default='education'  # Default type if not specified
    )
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

