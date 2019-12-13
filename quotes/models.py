from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class QuoteManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['quote']) < 10:
            errors['quote'] = "quote must be at least 10 characters"
        if len(postData['author']) < 3:
            errors['author'] = "Author name must be at least 3 characters"
        return errors

class Quote(models.Model):
    quote=models.TextField()
    author=models.CharField(max_length=150)
    poster=models.ForeignKey(User,related_name="quotes", on_delete=models.CASCADE)
    favouriting_users= models.ManyToManyField(User, related_name="favourite_quotes")
    objects = QuoteManager() 

class Quote_Liked(models.Model):
    quote_liked=models.ForeignKey(Quote,related_name="liked", on_delete=models.CASCADE) 
    liked_by=models.ForeignKey(User,related_name="like_quote", on_delete=models.CASCADE) 


