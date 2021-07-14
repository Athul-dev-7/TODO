

from django.urls.conf import path
from  django.urls import path
from . import views
import tasks

urlpatterns = [
    path('',views.index,name='list'),
    path('update/<str:pk>',views.updateTask,name='update'),
    path('delete/<str:pk>',views.deleteTask,name='delete')
]