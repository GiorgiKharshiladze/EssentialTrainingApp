from backend.models import *
from backend.serializers import *
from backend.helpers import question_maker as qm
from django.db.models import Avg, F
import json, time

# * ================ *
# * GET REQUESTS API *
# * ================ *

def test():
	return avg_time_to_finish(7)

def all_courses():
	"""Return serialized all Course objects"""
	return CourseSerializer(Course.objects.all(),many=True).data

def students_by_course(course_id):
	"""Return a list of students with a specific course_id"""
	return Student.objects.values_list('hash', flat=True).filter(course_id=course_id)

def logs_by_quiz(quiz_id):
	return QuizLogSerializer(QuizLog.objects.all().filter(quiz_id=quiz_id), many=True).data

def new_question(question_template_id):
	question_template_obj = QuestionTemplateSerializer(QuestionTemplate.objects.get(pk=question_template_id)).data
	question_template = json.loads(question_template_obj["template_json"])
	return qm.get_new_question_instance(question_template)

def all_students():
	"""Return serialized all student objects"""
	return StudentSerializer(Student.objects.all(), many=True).data

def student_details(hash):
	"""Return serialized student object by hash"""
	return StudentSerializer(Student.objects.get(pk=hash)).data

def all_question_templates():
	"""Return serialized all question templates"""
	question_template_objects = QuestionTemplate.objects.all()
	all_templates = []
	for qto in question_template_objects:
		json_object = {"id":qto.id,"type":qto.type,"template_json":json.loads(qto.template_json)}
		all_templates.append(json_object)
	return all_templates


def quiz_details(quiz_id):
	"""Return the JSON of quiz details"""
	quiz_obj = Quiz.objects.get(pk=quiz_id)
	details = {"title":quiz_obj.title, "questions":[],"is_published":quiz_obj.is_published}
	questions = json.loads(quiz_obj.question_json)
	for template_id, amount in questions.items():
		template_obj = QuestionTemplate.objects.get(pk=template_id)
		details['questions'].append({"template_id":int(template_id),"type":template_obj.type,"amount":amount})
	return details

def generate_hashes(amount, course_id):
	"""Generate a json student hashes based on the amount of students(int) and the course_id"""
	hashes = []
	my_hash = 0
	course = Course.objects.get(pk=course_id)
	for i in range(amount):
		my_hash = (course.title +" "+ course.semester).lower().replace(' ', "-") + "-" + str(hash(time.time()))
		serializer = StudentSerializer(data={"hash":my_hash,"course_id":course_id})
		if serializer.is_valid(): # if data matches all the columns
			serializer.save() # insert into db
		hashes.append(my_hash)
		time.sleep(0.001) # sleep for a bit to let it make the time.time() value unique
	return {"hashes":hashes,"course_id":course_id}

def quizzes_by_student(student_hash):
	student_obj = StudentSerializer(Student.objects.get(pk = student_hash)).data
	all_quizzes = quizzes_by_course(student_obj['course_id'])

	# TODO: THIS NEEDS TO BE FIXED
	old_quiz_list = completed_quizzes(student_hash)
	new_quiz_list = []

	for quiz in all_quizzes:
		if quiz not in old_quiz_list:
			new_quiz_list.append(quiz)

	return {"old":old_quiz_list,"new":new_quiz_list}

def quizzes_by_course(course_id):
    quizzes_queryset = Quiz.objects.filter(course_id=course_id)
    quizzes = []
    for quiz in quizzes_queryset:
        quiz_json = {'id':quiz.id,'title':quiz.title,'created_on' :quiz.created_on}
        quizzes.append(quiz_json)
    return quizzes

def quiz_stats(quiz_id):
	"""TODO: THIS WILL RETURN THE STATS JSON WHEN IT'S DONE"""
	return quiz_id


# * =============== *
# * HELPER QUERIES  *
# * =============== *

def completed_quizzes(student_hash):
	"""Return quiz_ids for quizzes that are completed by a specific student"""
	quiz_ids = QuizLog.objects.values_list('quiz_id', flat=True).filter(student_hash=student_hash, completed=True)

	quizzes_queryset = Quiz.objects.filter(pk__in=quiz_ids)

	quizzes = []
	for quiz in quizzes_queryset:
		quiz_json = {'id':quiz.id,'title':quiz.title,'created_on' :quiz.created_on}
		quizzes.append(quiz_json)
	return quizzes

def quiz_overview(quiz_id):
	"""This method is used for displaying stats in quiz_stats function"""
	overview = {}
	quiz_obj = Quiz.objects.get(pk=quiz_id)
	data = json.loads(QuizSerializer(quiz_obj).data['question_json'])
	for key in data.keys():
		question_type = QuestionTemplate.objects.get(pk=int(key)).type
		overview[question_type] = data[key]
	return overview

def avg_time_to_finish(quiz_id):
	"""This method is used for displaying stats in quiz_stats function"""
	diffs = []
	logs = QuizLog.objects.filter(quiz_id=quiz_id, completed=True, passed=True)
	for log in logs:
		diffs.append((log.end_time - log.start_time).total_seconds())
	return {"average_time":sum(diffs)/float(len(diffs))} # average time in seconds

