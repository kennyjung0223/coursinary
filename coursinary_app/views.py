from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages

from .models import Subject, Course
from .forms import CourseForm, EntryForm

from titlecase import titlecase

""" not to be added yet until final version
if not Subject.objects.all():
	filename1 = 'coursinary_app/course_files/subjects.txt'
	filename2 = 'coursinary_app/course_files/subject_codes.txt'

	with open(filename1) as f:
		subjects = f.readlines()

	with open(filename2) as f:
		subject_codes = f.readlines()

	for i in range(len(subjects)):
		Subject.objects.create(text=subjects[i].rstrip(), code=subject_codes[i].rstrip())"""

def index(request):
	"""The home page for Coursinary"""
	return render(request, 'coursinary_app/index.html')

def subjects(request):
	"""Show all subjects"""
	subjects = Subject.objects.order_by('id')
	context = {'subjects': subjects}
	return render(request, 'coursinary_app/subjects.html', context)

def subject(request, subject_code):
	"""Show all courses in a particular subject"""
	if not Course.objects.all().exists():
		raise Http404

	courses = Course.objects.filter(code=subject_code).order_by('course_number')
	context = {'courses': courses, 'subject_code': subject_code}
	return render(request, 'coursinary_app/subject.html', context)

def course(request, course_code, course_course_number):
	"""Show a single course and all its entries"""
	course = get_object_or_404(Course, code=course_code, course_number=course_course_number)
	entries = course.entry_set.order_by('-date_added')
	context = {'course': course, 'entries': entries}
	return render(request, 'coursinary_app/course.html', context)

def new_course(request, subject_code):
	"""Add a new course for a subject"""
	subject = get_object_or_404(Subject, code=subject_code)

	if request.method != 'POST':
		# No data submitted; create a blank form
		form = CourseForm()
	else:
		# POST data submitted; process data
		form = CourseForm(data=request.POST)

		if form.is_valid():
			course_name = ''.join(titlecase(form['text'].data)).replace("Intro", "Introduction")
			course_number = ''.join(form['course_number'].data.title())

			while len(course_number) < 3:
				course_number = '0' + course_number

			course_name_exists =Course.objects.filter(code=subject_code).values_list('text').filter(text=course_name).exists()
			course_number_exists = Course.objects.filter(code=subject_code).values_list('course_number').filter(course_number=course_number).exists()

			if not form['course_number'].data[:3].isnumeric() or course_name_exists or course_number_exists:
				check_for_errors(request, form, course_name_exists, course_number_exists)	
				form = CourseForm()
			else:
				new_course = form.save(commit=False)
				new_course.subject = subject
				new_course.code = subject_code
				new_course.text = course_name
				new_course.course_number = course_number
				new_course.save()
				return redirect('coursinary_app:subject', subject_code=subject_code)

	# Display a blank or invalid form
	context = {'subject': subject, 'subject_code': subject.code, 'form': form}
	return render(request, 'coursinary_app/new_course.html', context)

def new_entry(request, course_code, course_course_number):
	"""Add a new entry for a course"""
	course = get_object_or_404(Course, code=course_code, course_number=course_course_number)

	if request.method != 'POST':
		# No data submitted; create a blank form
		form = EntryForm()
	else:
		# POST data submitted; process data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.course = course
			new_entry.save()
			return redirect('coursinary_app:course', course_code=course_code, course_course_number=course_course_number)

	# Display a blank or invalid form
	context = {'course': course, 'course_code': course.code, 'course_number': course.course_number, 'form': form}
	return render(request, 'coursinary_app/new_entry.html', context)

# Helper functions
def check_for_errors(request, form, course_name_exists, course_number_exists):
	if not form['course_number'].data[:3].isnumeric():
		messages.error(request, 'Invalid course number')

	elif course_name_exists:
		messages.error(request, 'That course name already exists')
			
	elif course_number_exists:
		messages.error(request, 'That course number already exists')
