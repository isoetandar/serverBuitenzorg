from __future__ import unicode_literals
from django.db import models
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class ValidatorManager(models.Manager):
      def Validator(self, postData):
        errors={}
        if len(postData['first_name']) < 3:
              errors['first_name'] = "First name field can't be blank and it should have at least 3 characters"
        if len(postData['last_name']) < 3:
              errors['last_name'] = "Last name can't be blank and it should should have at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):
              errors['email']= "Invalid Email Address!"
        if len(postData['password']) < 3:
              errors['password'] = "Password can't be blank and it should be have at least 3 characters"
        if postData['password'] != postData['confirmPassword']:
              errors['unmatch'] = "Your type unmatch confirm password"
        return errors
      
      def UpdateValidator(self, postData):
        errors_update={}
        if len(postData['first_name']) < 3:
              errors_update['first_name'] = "First name field can't be blank and it should have at least 3 characters"
        if len(postData['last_name']) < 3:
              errors_update['last_name'] = "Last name can't be blank and it should should have at least 3 characters"
        if not EMAIL_REGEX.match(postData['email']):
              errors_update['email']= "Invalid Email Address!"
        return errors_update

      def QuoteValidator(self, postData):
            errors_quote={}
            if len(postData['author']) < 3:
                  errors_quote ['author'] = "Author field can't be blank and it should have at least 3 characters"
            if len(postData['quote_text']) < 10:
                  errors_quote ['quote_text'] = "Quote field can't be blank and it should have at least 10 characters"
            return errors_quote

class User(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = ValidatorManager()

class Quote(models.Model):
      author = models.CharField(max_length=255)
      posted_by = models.ForeignKey(User, related_name="quotes")
      quote_text = models.CharField(max_length=255)
      likes_by = models. ManyToManyField(User, related_name="like")
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = ValidatorManager()