from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the home index.")


def science(request):
    return HttpResponse("Hello, world. You're at science")


def technology(request):
    return HttpResponse("Hello, world. You're at technology")


def engineering(request):
    return HttpResponse("Hello, world. You're at engineering")


def arts(request):
    return HttpResponse("Hello, world. You're at arts")


def mathematics(request):
    return HttpResponse("Hello, world. You're at mathematics")
