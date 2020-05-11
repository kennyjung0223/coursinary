from django import forms

from .models import Course, Entry

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = [
				  'text', 
				  'code', 
				  'course_number'
				  ]
		labels = {
				  'text': 'Course Name', 
				  'code': 'Subject Code', 
				  'course_number': 'Course Number'
				  }
		widgets = {
				  'text': forms.TextInput(attrs={'placeholder': 'i.e. ABC 123: Example Course'}),
				  'code': forms.TextInput(attrs={'placeholder': 'i.e. ABC'}),
				  'course_number': forms.TextInput(attrs={'placeholder': 'i.e. 123'}),
				  }

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': 'You can expect this class to be...'}),}