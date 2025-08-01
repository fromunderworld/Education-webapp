from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "cv/index.html")

def leaveacomment(request, comment):
    return render(request, "cv/comment.html", {
        "comment": comment.capitalize()
    })