from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.helpers import get, post


@api_view(["GET"])
def student_list_view(request):
	"""Return JSON response of all students"""
	return Response(get.all_students())

@api_view(["GET"])
def student_details_view(request, hash):
	"""Return JSON response of student details by hash"""
	return Response(get.student_details(hash))

@api_view(["GET"])
def quiz_details_view(request, quiz_id):
	"""Return JSON response of quiz details"""
	return Response(get.quiz_details(quiz_id))

@api_view(["GET"])
def hash_generator_view(request, amount, course_id):
	"""Return and create hashes in the database"""
	return Response(get.generate_hashes(amount, course_id))


@api_view(["POST"])
def create_quiz_view(request):
    return Response(post.create_quiz(request.data))

@api_view(['POST'])
def create_question_template_view(request):
	return Response(post.create_question_template(request.data))