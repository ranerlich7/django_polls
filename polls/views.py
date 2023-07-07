from django.http import HttpResponse

from polls.models import Question


def index(request):
    all_questions = Question.objects.all()[0]
    return HttpResponse(f"Hello, Ran! You're at the polls index.\n Thess are the questions:\n{all_questions}")

def create(request):
    
    return HttpResponse("POLL CREATED.")

def delete(request):
    return HttpResponse("POLL DELETED")
