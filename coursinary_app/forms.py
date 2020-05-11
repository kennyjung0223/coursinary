from django import forms

from .models import Subject, Course, Entry

CODE_CHOICES = (
	('i.e. ABC', 'i.e. ABC'),
	('ANTH', 'ANTH'), ('BIO', 'BIO'),
	('BIOE', 'BIOE'), ('CCST', 'CCST'),
	('CHEM', 'CHEM'), ('CHN', 'CHN'),
	('COGS', 'COGS'), ('CRES', 'CRES'),
	('CRS', 'CRS'), ('CSE', 'CSE'),
	('ECON', 'ECON'), ('EECS', 'EECS'),
	('ENG', 'ENG'), ('ENGR', 'ENGR'),
	('ENVE', 'ENVE'), ('ES', 'ES'),
	('ESS', 'ESS'), ('FRE', 'FRE'),
	('GASP', 'GASP'), ('HIST', 'HIST'),
	('HS', 'HS'), ('IH', 'IH'),
	('JPN', 'JPN'), ('MATH', 'MATH'),
	('MBSE', 'MBSE'), ('ME', 'ME'),
	('MGMT', 'MGMT'), ('MIST', 'MIST'),
	('MSE', 'MSE'), ('NSED', 'NSED'),
	('PH', 'PH'), ('PHIL', 'PHIL'),
	('PHYS', 'PHYS'), ('POLI', 'POLI'),
	('PSY', 'PSY'), ('QSB', 'QSB'),
	('SOC', 'SOC'), ('SPAN', 'SPAN'),
	('SPRK', 'SPRK'), ('WRI', 'WRI'),
	)

class CourseForm(forms.ModelForm):
	#code = forms.ModelChoiceField(queryset=Subject.objects.values_list('code', flat=True))

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
				  'code': forms.Select(choices=CODE_CHOICES),
				  'course_number': forms.TextInput(attrs={'placeholder': 'i.e. 123'}),
				  }

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80, 'placeholder': 'You can expect this class to be...'}),}















		