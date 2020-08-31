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

class CV(models.Model):
    title = models.CharField(max_length=200, default = "Oscar's CV")
    email = models.CharField(max_length = 50, blank = True, null = True)
    phone = models.CharField(max_length = 15, blank = True, null = True)
    personal_profile = models.TextField(blank = True, null = True)
    interests = models.TextField(blank = True, null = True)
    #skills = skill name, description and proficiency, table?
    #education = table
    #Employment/Work Experience
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title
