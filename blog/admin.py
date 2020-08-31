from django.contrib import admin
from .models import Post, CV, WorkExperience, Qualifications, Skills 

# Register your models here.
admin.site.register(Post)
admin.site.register(CV)
admin.site.register(WorkExperience)
admin.site.register(Qualifications)
admin.site.register(Skills)