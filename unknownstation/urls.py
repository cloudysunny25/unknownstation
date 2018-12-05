from django.urls import include, path
from . import views

app_name = 'unknownstation'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/detail/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.logout, name='logout'),
    path('<int:post_id>/updateView/', views.updateView, name='updateView'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
