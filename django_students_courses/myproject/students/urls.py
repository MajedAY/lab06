from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('add_student/', views.students, name='add_student'),
    path('<int:student_id>/', views.details, name='details'),
    path('add_course/', views.courses, name='add_course'),
    path('courses/', views.courses, name='courses'),  
]
from django.urls import path
from . import views

