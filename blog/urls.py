from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv/', views.view_cv, name ='cv'),
    path('cv/edit/', views.cv_edit, name = 'cv_edit'),
    path('cv/work/', views.work_new, name = 'new_work'),
    path('cv/skill/', views.skill_new, name = 'new_skill'),
    path('cv/qual/',views.qual_new, name = 'new_qual'),
    path('cv/work/<int:pk>/edit/', views.work_edit, name = 'edit_work')
]