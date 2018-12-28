from django.urls import include, path
from . import views

app_name = 'unknownstation'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/<int:page>/', views.postlist, name='list'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('register/', views.register, name='register'),
    path('login/', views.__login__, name='login'),
    path('auth/', views.auth, name='auth'),
    path('logout/', views.__logout__, name='logout'),
    path('updateView/<int:post_id>/', views.updateView, name='updateView'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('category/<str:category>/<int:page>', views.byCategory, name='byCategory'),
    path('search/', views.byKeyword, name='byKeyword'),
    path('category/', views.category, name='category'),
    path('month/', views.month, name='month'),
    path('month/<int:year>/<int:month>/<int:page>', views.byMonth, name='byMonth'),


]
