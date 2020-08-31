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
        widgets = {
        'start_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'end_date': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualifications
        fields = ['qualification', 'date_achieved',]
        widgets = {
            'date_achieved': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill', 'proficiency',]
