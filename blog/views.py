from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, CV, WorkExperience, Qualifications, Skills
from .forms import PostForm, CVForm, WorkForm, QualificationForm, SkillsForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return redirect('/')

def post_edit(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return redirect('/')

def cv_edit(request):
    cv = get_object_or_404(CV)
    if request.method == "POST":
        form = CVForm(request.POST, instance = cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.save()
            return redirect('cv')
    else:
         form = CVForm(instance = cv)
    return render(request, 'blog/cv_edit.html', {'form': form})

def work_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = WorkForm(request.POST)
            if form.is_valid():
                work = form.save(commit=False)
                work.save()
                return redirect('new_work')
        form = WorkForm()
        workdisplay = WorkExperience.objects.all()
        context = {
            'form' : form,
            'worktable' : workdisplay,
        }
        return render(request,"blog/work_edit.html",context)
    else:
        return redirect('cv')

def work_edit(request, pk):
    if request.user.is_authenticated:
        work = get_object_or_404(WorkExperience, pk = pk)
        if request.method == "POST":
            form = WorkForm(request.POST, instance = work)
            if form.is_valid():
                work = form.save(commit=False)
                work.save()
                return redirect('new_work')
        else:
            form = WorkForm(instance = work)
        return render(request, "blog/cv_edit.html", {'form': form})

def skill_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SkillsForm(request.POST)
            if form.is_valid():
                skill = form.save(commit=False)
                skill.save()
                return redirect('new_skill')
        form = SkillsForm()
        skilldisplay = Skills.objects.all()
        context = {
            'form' : form,
            'skilltable' : skilldisplay,
        }
        return render(request,"blog/new_skill.html",context)
    else:
        return redirect('cv')

def skill_edit(request, pk):
    if request.user.is_authenticated:
        skill = get_object_or_404(Skills, pk = pk)
        if request.method == "POST":
            form = SkillsForm(request.POST, instance = skill)
            if form.is_valid():
                skill = form.save(commit=False)
                skill.save()
                return redirect('new_skill')
        else:
            form = SkillsForm(instance = skill)
        return render(request, "blog/cv_edit.html", {'form': form})


def qual_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = QualificationForm(request.POST)
            if form.is_valid():
                qual = form.save(commit=False)
                qual.save()
                return redirect('new_qual')
        form = QualificationForm()
        qualdisplay = Qualifications.objects.all()
        context = {
            'form' : form,
            'qualtable' : qualdisplay,
        }
        return render(request,"blog/new_qual.html",context)
    else:
        return redirect('cv')

def qual_edit(request, pk):
    if request.user.is_authenticated:
        qual = get_object_or_404(Qualifications, pk = pk)
        if request.method == "POST":
            form = QualificationForm(request.POST, instance = qual)
            if form.is_valid():
                qual = form.save(commit=False)
                qual.save()
                return redirect('new_qual')
        else:
            form = QualificationForm(instance = qual)
        return render(request, "blog/cv_edit.html", {'form': form})

def view_cv(request):
    cv = get_object_or_404(CV)
    workdisplay = WorkExperience.objects.all()
    qualdisplay = Qualifications.objects.all()
    skilldisplay = Skills.objects.all()

    return render(request,"blog/cv_detail.html",{"worktable": workdisplay,"qualtable":qualdisplay,"skilltable":skilldisplay, "cv":cv})
