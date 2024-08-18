from django.urls import path
from todo_app import views

urlpatterns = [
    # CREATE a New Task
    path('addtask/', views.addtask, name='addTask'),
    # MARK as Done
    path('mark_done/<int:pk>/', views.mark_done, name='mark_done'),
    # MARK as Undone
    path('mark_as_incomplete/<int:pk>/', views.mark_as_incomplete, name='mark_as_incomplete'),
    # DELETE Task
    path('del/<int:pk>/', views.remove, name='del'),
    # EDIT Task
    path('update/<int:pk>/', views.update, name='update'),
]