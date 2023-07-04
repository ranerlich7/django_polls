from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Ran! You're at the polls index.")

def create(request):
    return HttpResponse("POLL CREATED.")

def delete(request):
    return HttpResponse("POLL DELETED")
