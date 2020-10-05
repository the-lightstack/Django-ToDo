from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from ToDoApp.data_base_handling import get_lists,get_tasks_by_list_id,get_list_by_id
# Create your views here.

def index(request):
    #template=loader.get_template("ToDoApp/index.html")
    #return HttpResponse("test still working")
    return render(request,"ToDoApp/index.html")

def edit(request):
    lists=get_lists()
    print("Lists:",lists)
    
    return render(request,"ToDoApp/edit.html",{"lists":lists})

def show_list(request,list_id):
    print("request:",request)
   
    #have to fix csrf token stuff later lol
    tasks=get_tasks_by_list_id(list_id)
    if len(tasks)==0:
        return HttpResponse("No lists available here.")
    list_name=get_list_by_id(list_id)
    return render(request,"ToDoApp/edit_list.html",{"tasks":tasks,"list":list_name})