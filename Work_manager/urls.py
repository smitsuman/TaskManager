from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import CreateView
from TaskManager.models import Project
from TaskManager.models import Project, Task
from TaskManager.models import Project
from django.views.generic.list import ListView
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', 'TaskManager.views.index.page'),
    url(r'^index$', 'TaskManager.views.index.page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^connection$', 'TaskManager.views.connection.page', name= "jhatu"),
    url(r'^project-detail-(?P<pk>\d+)$', 'TaskManager.views.project_detail.page', name="project_detail"),
    url(r'^create_developer$', 'TaskManager.views.create_developer.page', name="create_developer"),
    url(r'^create-supervisor$', 'TaskManager.views.create_supervisor.page', name="create_supervisor"),
    url (r'^create_project$', CreateView.as_view(model=Project, template_name="en/public/create_project.html", success_url = 'index'),name="create_project"),
    url (r'^create_task$', CreateView.as_view(model=Task, template_name="en/public/create_task.html", success_url = 'index'), name="create_task"),
    url (r'^project_list$', ListView.as_view(model=Project, template_name="en/public/project_list.html"), name="project_list"),
    url (r'^task_detail_(?P<pk>\d+)$', 'TaskManager.views.task_detail.page', name="task_detail"),

)
