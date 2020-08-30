from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from programs.models import Programs
from user_profile.models import Profile
from django.contrib.auth.models import User


class Testimonials(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    review = models.TextField(max_length=2064)
    score = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    date = models.DateField()
