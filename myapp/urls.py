from django.urls import path
from .import views

urlpatterns=[
	path('', views.home, name='home'),
	path('register/',views.register, name='register'),
	path('login/', views.loginuser, name='login'),
	path('logout/', views.logoutuser, name='logout'),
	path('add_show/', views.showdetails, name='add_show'),
	path('update/<str:pk>/', views.updatedetails, name='update'),
	path('delete/<str:pk>/',views.delete, name='delete')
]