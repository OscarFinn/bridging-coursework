from django import forms
from .models import Post, CV, WorkExperience, Qualifications, Skills

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['title', 'text',]

class CVForm(forms.ModelForm):
    class Meta:
        model= CV
        fields = ['personal_profile','interests','phone', 'email',]

class WorkForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['position', 'start_date', 'end_date', 'description',]

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualifications
        fields = ['qualification', 'date_achieved',]

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill', 'proficiency',]