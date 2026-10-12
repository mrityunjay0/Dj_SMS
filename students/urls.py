from django.urls import path

from . import views

urlpatterns = [

    path('', views.students_list, name='students_list'),
    path('add/', views.create_student, name='create_student'),
    path('<int:id>/', views.student_detail, name='student_detail'),
    path('<int:id>/edit/', views.student_update, name='student_update'),
    path('<int:id>/delete/', views.student_delete, name='student_delete'),

]