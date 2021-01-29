from django import forms
from django.shortcuts import render

tasks = ["abc","def","ghi"]

class NewTaskForm(forms.Form):
    task = forms.CharField(max_length=255,label='New Task')
    priority = forms.IntegerField(label="Priority",min_value=1,max_value=5)


def index(request):
    return render(request,"tasks/index.html", {
        "tasks": tasks
    }) 

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    return render(request,"tasks/add.html",{
        "form": NewTaskForm()
    })