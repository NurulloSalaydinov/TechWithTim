from django import forms
from main.models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = '__all__'


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class SettingForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = '__all__'


