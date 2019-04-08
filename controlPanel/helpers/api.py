from controlPanel.models import Student, Quiz, Course, QuestionTemplate, QuizLog
import json

def get_quiz_details_json(quiz_id):
	quiz_obj = Quiz.objects.get(pk=quiz_id)
	print(quiz_obj.title)
	# TODO: Check if this hash is registered for this course and if this quiz allowed
	details = {"title":quiz_obj.title, "questions":[],"is_published":quiz_obj.is_published}
	questions = json.loads(quiz_obj.question_json)
	for template_id, amount in questions.items():
		template_obj = QuestionTemplate.objects.get(pk=template_id)
		details['questions'].append({"template":json.loads(template_obj.template_json),"type":template_obj.type,"amount":amount})

	return details
