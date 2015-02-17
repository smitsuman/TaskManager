from django.shortcuts import render
from TaskManager.models import Project
from TaskManager.models import Project, Task, Supervisor, Developer
from django.shortcuts import render
from django.utils import timezone
# - * - Coding: utf -8 - * -
# View for index page.
# Create your views here.
"""
View for index page.
"""
 # line 1

def page(request):
    new_project = Project(title="Tasks Manager with Django",
    description="Django project to getting start with Django easily.", client_name="Me") # line 2
    new_project.save() # line 3
    return render(request, 'en/public/index.html', {'action':'Save datas of model'})


def page(request):
# Saving a new supervisor
    new_supervisor = Supervisor(name="Guido van Rossum", login="python", password="password", last_connection=timezone.now(), email="python@python.com", specialisation="Python") # line 1
    new_supervisor.save()
# Saving a new developer
    new_developer = Developer(name="Me", login="me", password="pass", last_connection=timezone.now(), email="me@python.com", supervisor=new_supervisor)
    new_developer.save()
# Saving a new task
    project_to_link = Project.objects.get(id = 1) # line 2
    new_task = Task(title="Adding relation", description="Example of adding relation and save it", time_elapsed=2, importance=0, project=project_to_link, developer=new_developer) # line 3
    new_task.save()
    return render(request, 'en/public/index.html', {'action' : 'Save relationship'})

def page(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'en/public/project_detail.html', {'project' :project})