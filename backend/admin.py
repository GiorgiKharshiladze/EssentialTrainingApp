from django.contrib import admin
from backend.models import *

# Register your models here.
admin.site.register([Student, Quiz, Course, QuestionTemplate, QuizLog])