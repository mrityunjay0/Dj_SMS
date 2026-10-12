from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'name',
            'age',
            'english_marks',
            'maths_marks',
        ]


        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter student name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age',
                'min': 1,
                'max': 120
            }),
            'english_marks': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter English marks',
                'min': 0,
                'max': 100
            }),
            'maths_marks': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Maths marks',
                'min': 0,
                'max': 100
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError(
                "Student name cannot be empty."
            )
        return name

    def clean_age(self):
        age = self.cleaned_data['age']
        if not 1 <= age <= 120:
            raise forms.ValidationError(
                "Age must be between 1 and 120."
            )
        return age

    def clean_english_marks(self):
        marks = self.cleaned_data['english_marks']
        if not 0 <= marks <= 100:
            raise forms.ValidationError(
                "English marks must be between 0 and 100."
            )
        return marks

    def clean_maths_marks(self):
        marks = self.cleaned_data['maths_marks']
        if not 0 <= marks <= 100:
            raise forms.ValidationError(
                "Maths marks must be between 0 and 100."
            )
        return marks