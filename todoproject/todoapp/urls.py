from . import views
from django.urls import path

urlpatterns = [
    path('cbvhome/', views.homeview.as_view(), name='homeview'),
    path('cbvDetail/<int:pk>/', views.TaskDetailView.as_view(), name='detailview'),
    path('cbvUpdate/<int:pk>/', views.TaskUpdateView.as_view(), name='updateview'),
    path('cbvDelate/<int:pk>/', views.TaskDeleteView.as_view(), name='deleteview'),

    path('', views.home, name='home'),
    path('update/<int:id>/', views.update, name='update'),
    path('confirm_delete/<int:taskid>/',
         views.confirm_delete, name='confirm_delete'),

]
