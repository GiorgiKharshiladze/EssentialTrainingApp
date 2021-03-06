# Essential Training App


## List of Apis:
djangoAdmin/ \
api/ students/ \
api/ students/<str:hash>/ \
api/ students/course/<int:course_id>/ \
api/ quizzes/<int:quiz_id>/ \
api/ quizzes/hash/<str:hash>/ \
api/ quizzes/course/<int:course_id>/ \
api/ hashes/<int:amount>/<int:course_id>/ \
api/ question/new/<int:question_template_id>/ \
api/ courses/ \
api/ logs/quiz/<int:quiz_id>/ \
api/ create/quiz/ \
api/ create/quiz_log/ \
api/ create/question_template/ 

___
### Following POST requests return `{"success":True/False}`<br>
* ### Create a new quiz:
> **Callback url:** `/api/create/quiz` with data:<br>
> `
{
	"title":"New Quiz",
	"question_json":"{'1':5,'2':9}",
	"is_published":1,
	"course_id":2
}
`<br>

* ### Create a new question template:
> **Callback url:** `/api/create/question_template` with data:<br>
> `
{
	"type":"Vector Addition",
	"template_json":"{'inputs':['a','b'], 'outputs':['a+b', 'a-b'], 'input_type':'regular','text':'I have $ apples, somebody gave me $ apples. How many apples do I have?','output_template':'A = <$, $>','input_values':[[1,100],[100,200]]}"
}
`<br>
___

### GET requests <br>
* ### Get quiz details
> **Callback url:** `/api/quizzes/<int:quiz_id>`