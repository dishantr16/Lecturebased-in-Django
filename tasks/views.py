from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=255,label='New Task')
    priority = forms.IntegerField(label="Priority",min_value=1,max_value=5)


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request,"tasks/index.html", {
        "tasks": request.session["tasks"]
    }) 

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if not form.is_valid():
            return render(request,"tasks/add.html",{
                "form":form
            })
        task = form.cleaned_data["task"]
        request.session["tasks"] += [task]
        return HttpResponseRedirect(reverse("tasks:index"))
    return render(request,"tasks/add.html",{
        "form": NewTaskForm()
    })