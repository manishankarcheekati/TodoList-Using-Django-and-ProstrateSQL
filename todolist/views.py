from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList, Category
import datetime

def index(request):
	todos = TodoList.objects.all() 
	categories = Category.objects.all() 
	if request.method == "POST":
		if "taskAdd" in request.POST: 
			title = request.POST["description"]
			date = str(request.POST["date"])
			category = request.POST["category_select"] 
			content = title + " -- " + date + " " + category
			Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
			Todo.save() #saving the todo 
			return redirect("/") 
		
		if "taskDelete" in request.POST: 
			checkedlist = request.POST["checkedbox"] 
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) 
				todo.delete() #deleting todo

	return render(request, "index.html", {"todos": todos, "categories":categories})
