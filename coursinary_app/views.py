from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib import messages

from .models import Subject, Course
from .forms import CourseForm, EntryForm

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
			course_name_exists = Course.objects.filter(code=subject_code).values_list('text').filter(text=form['text'].data.title()).exists()
			course_number_exists = Course.objects.filter(code=subject_code).values_list('course_number').filter(course_number=form['course_number'].data).exists()

			if not form['course_number'].data.isnumeric:
				form = CourseForm()
				messages.error(request, 'Invalid course number')
				
			elif course_name_exists and course_number_exists:
				form = CourseForm()
				messages.error(request, 'That course already exists')
			
			elif course_name_exists:
				form = CourseForm()
				messages.error(request, 'That course name already exists')
			
			elif course_number_exists:
				form = CourseForm()
				messages.error(request, 'That course number already exists')
			
			else:
				new_course = form.save(commit=False)
				new_course.subject = subject
				new_course.code = subject_code
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


