from django.urls import path

from . import views
import ToDoApp.data_base_handling as dbh
dbh.setup_db()

urlpatterns = [
    path('', views.index),#, name='index'),
    path('edit/',views.edit),
    path("edit/<int:list_id>",views.show_list)
]