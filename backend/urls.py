from django.conf.urls import url
from django.urls import path
from backend import api


urlpatterns = [
	# TEST METHOD
	path('test/', api.test_view),
	# GET METHODS
	path('students/', api.student_list_view),
	path('students/<str:hash>/', api.student_details_view),
	path('students/course/<int:course_id>/', api.students_by_course_view),

	path('quizzes/<int:quiz_id>/', api.quiz_details_view),
	path('quizzes/student/<str:hash>/', api.quizzes_by_student_view),
	path('quizzes/course/<int:course_id>/', api.quizzes_by_course_view),

	path('hashes/<int:amount>/<int:course_id>/', api.hash_generator_view),
	path('question/new/<int:question_template_id>/', api.new_question_view),
	path('question/templates/', api.question_template_list_view),
	path('courses/', api.all_courses_view),
	path('logs/quiz/<int:quiz_id>/', api.logs_by_quiz_view),

	path('stats/quiz/<int:quiz_id>/', api.quiz_stats_view),

	# POST METHODS
	path('create/quiz/', api.create_quiz_view),
	path('create/quiz_log/', api.create_quiz_log_view),
	path('create/question_template/', api.create_question_template_view)
]
