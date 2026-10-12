from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Student
from .forms import StudentForm


# Create your views here.

# get all students
def students_list(request):
    students = Student.objects.all().order_by('id')

    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )

# create student
def create_student(request):
    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,'Student added successfully.'
            )

            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {
            'form': form,
            'title': 'Add Student',
            'button_text': 'Add Student'
        }
    )


# get student by id
def student_detail(request, id):
    student = get_object_or_404(Student, id = id)

    return render(
        request,
        'students/student_detail.html',{'student': student}
    )


def student_update(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Student updated successfully.'
            )

            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'students/student_form.html',
        {
            'form': form,
            'title': 'Update Student',
            'button_text': 'Save Changes'
        }
    )


def student_delete(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        student.delete()

        messages.success(
            request,
            'Student deleted successfully.'
        )

        return redirect('student_list')

    return render(
        request,
        'students/student_confirm_delete.html',
        {'student': student}
    )
