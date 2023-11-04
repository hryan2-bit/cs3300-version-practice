from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),

path('killers/', views.KillerListView.as_view(), name='killers'),
path('killers/<int:pk>', views.KillerDetailView.as_view(), name='killer-detail'),
path('users/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
path('users/create', views.createUser, name='create_user'),
path('users/<int:user_id>/killers/update', views.updateKillerList, name='update_killers'),
path('users/<int:user_id>/delete', views.deleteUser, name='delete_user'),
]