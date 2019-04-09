from backend.models import *
from backend.serializers import *

# * ================= *
# * POST REQUESTS API *
# * ================= *

def create_quiz(data):
	serializer = QuizSerializer(data=data)
	if serializer.is_valid():
		serializer.save()
	return {"success":serializer.is_valid()}