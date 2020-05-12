from django import forms
#from captcha.fields import ReCaptchaField

from .models import Subject, Course, Entry

class CourseForm(forms.ModelForm):
	#code = forms.ModelChoiceField(queryset=Subject.objects.values_list('code', flat=True))
	#captcha = ReCaptchaField()

	class Meta:
		model = Course
		fields = [
				  'course_name', 
				  'course_number'
				  ]
		labels = {
				  'course_name': 'Course Name', 
				  'course_number': 'Course Number'
				  }
		widgets = {
				  'course_name': forms.TextInput(attrs={'placeholder': 'i.e. Example Course'}),
				  'course_number': forms.TextInput(attrs={'placeholder': 'i.e. 123'}),
				  }

class EntryForm(forms.ModelForm):
	#captcha = ReCaptchaField()
	
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': 'You can expect this class to be...'}),}

