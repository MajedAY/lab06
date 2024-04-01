from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Course
from .forms import StudentForm, CourseForm, StudentCourseForm


def students(request):
    students = Student.objects.all()
    courses = Course.objects.all()  

    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('students')
    else:
        student_form = StudentForm()

    context = {'students': students, 'courses': courses, 'student_form': student_form}
    return render(request, 'students/students.html', context)

def courses(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('courses')
    else:
        course_form = CourseForm()

    context = {'courses': courses, 'course_form': course_form}
    return render(request, 'students/courses.html', context)

def details(request, student_id):
    student = Student.objects.get(pk=student_id)
    available_courses = Course.objects.exclude(students=student)  

    if request.method == 'POST':
        course_form = StudentCourseForm(request.POST)
        if course_form.is_valid():
            course = course_form.cleaned_data['course']
            student.courses.add(course)
            messages.success(request, 'Course added to student successfully!')
            return redirect('details', student_id)
    else:
        course_form = StudentCourseForm(initial={'student': student})

    context = {'student': student, 'available_courses': available_courses, 'course_form': course_form}
    return render(request, 'students/details.html', context)
