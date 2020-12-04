from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def validatorRegister(self, postData):
        errors = {}
        email = postData['email']
        emailRegex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['firstName']) < 2:
            errors['firstName'] = "is required"
        if postData['firstName'].isalpha() == False:
            errors['firstName'] = "must only contain alphabetical characters"
        if len(postData['lastName']) < 2:
            errors['lastName'] = "is required"
        if postData['lastName'].isalpha() == False:
            errors['lastName'] = "must only contain alphabetical characters"
        if not emailRegex.match(postData['email']):
            errors['email'] = "is an invalid format"
        if User.objects.filter(email=email):
            errors['emailInUse'] = "is already in use"
        if postData['password'] < 8:
            errors['password'] = "is too short"
        if postData['passwordMatch'] != postData['confirmPassword']:
            errors['passwordMatch'] = "passwords do not match"

class User(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)