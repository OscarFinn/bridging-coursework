from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#add a cv model here. 

class WorkExperience(models.Model):
    position = models.CharField(max_length = 200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table="worktable"
    def publish(self):
        self.save()

    def __str__(self):
        return self.position

class Skills(models.Model):
    skill = models.CharField(max_length=200)
    proficiency = models.CharField(max_length=200)
    class Meta:
        db_table="skilltable"
    def publish(self):
        self.save()

    def __str__(self):
        return self.skill

class Qualifications(models.Model):
    qualification = models.CharField(max_length = 200)
    date_achieved = models.DateField()
    class Meta:
        db_table="qualtable"
    def publish(self):
        self.save()

    def __str__(self):
        return self.qualification

class CV(models.Model):
    title = models.CharField(max_length=200, default = "Oscar's CV")
    email = models.CharField(max_length = 50, blank = True, null = True)
    phone = models.CharField(max_length = 15, blank = True, null = True)
    personal_profile = models.TextField(blank = True, null = True)
    interests = models.TextField(blank = True, null = True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

