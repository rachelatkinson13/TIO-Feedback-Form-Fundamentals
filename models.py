from django.db import models

# Create your models here.
class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    email_addresss = models.EmailField()
    feedback_message = models.TextField()