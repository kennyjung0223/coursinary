"""Defines URL patterns for coursinary_app"""

from django.urls import path

from . import views

app_name = 'coursinary_app'
urlpatterns = [
	# Home page
	path('', views.index, name='index'),
	# Page that shows all the subjects
	path('subjects', views.subjects, name='subjects'),
	# Page for a single subject
	path('subject/<str:subject_code>/', views.subject, name='subject'),
	# Page for single course
	path('subject/<str:course_code>/<str:course_course_number>/', views.course, name='course'),
	# Page for adding a new course
	path('new_course/<str:subject_code>/', views.new_course, name='new_course'),
	# Page for adding a new entry
	path('new_entry/<str:course_code>/<str:course_course_number>/', views.new_entry, name='new_entry'),
]