from django.http import HttpResponse

from polls.models import Choice, Question


def index(request):
    first_question = Question.objects.all()[0]
    return HttpResponse(f"Hello, Ran! You're at the polls index.\n Thess are the questions:\n{first_question}")

def create(request):
    
    return HttpResponse("POLL CREATED.")

def delete(request):
    return HttpResponse("POLL DELETED")


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    print(question)
    # details on the question. 
    return HttpResponse(f"You're looking at question id{question_id} : {question}")


def results(request, question_id):
    # get all choices from question. choice_set
    response = "You're looking at the results of question %s."
    
    # output = ", ".join([q.question_text for q in latest_question_list])

    return HttpResponse(response % question_id)


def vote(request, choice_id): # choiceID
    choice = Choice.objects.get(pk=choice_id)    
    choice.votes += 1
    choice.save()
    return HttpResponse("You're voting recieved on choice %s." % choice_id)

