from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from .forms import Add_Task_Form
from ToDoApp.data_base_handling import get_lists,get_tasks_by_list_id,get_list_by_id,add_task,remove_task,change_done,add_list,remove_list
# Create your views here.

def index(request):
    #template=loader.get_template("ToDoApp/index.html")
    #return HttpResponse("test still working")
    return render(request,"ToDoApp/index.html")

def edit(request):
    if request.method=="POST":
        print("POST-REQUEST:",request.POST)
        if request.POST.get("add_list"):
            print("post-req-stuff:",request.POST.get("add_list"))
            add_list(request.POST.get("add_list"))
        if request.POST.get("remove_list"):
            print("id_to_remove:",request.POST.get("to_remove_id"))
            remove_list(request.POST.get("to_remove_id"))
    lists=get_lists()
    #print("Lists:",lists)
    
    return render(request,"ToDoApp/edit.html",{"lists":lists})

def show_list(request,list_id):
   
   
    if request.method=="POST":
        #print("POST:",request.POST)
        form = Add_Task_Form(request.POST)
        if form.is_valid():
            
            add_task(list_id,form.cleaned_data)
            form=Add_Task_Form()

        if request.POST.get("delete_button"):
            task_id_to_remove=request.POST.get("task_id")
            remove_task(task_id_to_remove)

        if request.POST.get("change_done"):
            task_id=request.POST.get("task_id")
            change_done(task_id)
    else:
        form=Add_Task_Form()



    tasks=get_tasks_by_list_id(list_id)
    
    list_name=get_list_by_id(list_id)
    return render(request,"ToDoApp/edit_list.html",{"tasks":tasks,"list":list_name,"form":form})