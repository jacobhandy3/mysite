from django.db.models import query
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
import json
from .models import Task
from .forms import TaskForm

# Create your views here.
def TaskListCreate(request):
    '''
    Matched with url: /todo
    ------------------------
    If GET method passed, then returns a page with all the user's tasks and info

    If POST method passed, then creates task under user id
    otherwise return http forbidden b/c no user to create task under

    otheriwse return http bad request b/c no other methods will be accepted
    '''
    if request.user.id:
        if request.method == "GET":
            queryset = Task.objects.all().filter(creator=request.user.id)
            return render(request, "index.html", {"tasks": queryset})
        elif request.method == "POST":
            form = TaskForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                Task.objects.create(
                    creator=request.user,
                    title=data["title"],
                    details=data["details"],
                    date_due=data["date_due"],
                    priority=data["priority"]
                )
                return HttpResponse("Task Created!")
            else:
                return HttpResponseServerError()
        else:
            return HttpResponseBadRequest("METHOD NOT SUPPORTED!")
    else:
        return redirect("/")

def TaskDetail(request, pk):
    '''
    Matched with url: /todo/<int:pk>
    --------------------------------
    If GET method passed then grab the object with matching primary key
    and return a page with the object info

    if PUT method passed then get updated info from body
    and update object with it, then return new object or 404 response

    if DELETE method passed then get object and delete it,
    then return http response confirming task deleted

    other method passed, return bad request response

    otherwise return forbidden response
    '''
    if request.user.id:
        if request.method == "GET":
            return render(request,
            "task.html",
            {"task": get_object_or_404(Task, pk=pk)})
        elif request.method == "DELETE":
            rip = Task.objects.get(pk=pk)
            rip.delete()
            return HttpResponse("Task Deleted")
        else:
            return HttpResponseBadRequest("METHOD NOT SUPPORTED!")
    else:
        return redirect("/")
