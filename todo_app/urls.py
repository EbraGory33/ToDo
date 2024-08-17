from django.urls import path
from todo_app import views

urlpatterns = [
    path('addtask/', views.addtask, name='addTask'),
    path('del/<str:item_id>', views.remove, name="del"),
    path('update/', views.update, name='update')
]