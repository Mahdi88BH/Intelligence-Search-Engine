from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('process/', views.process_query, name='process'),
    path('history/<int:history_id>/', views.get_history_detail, name='history_detail'),
path('history/delete/<int:history_id>/', views.delete_history, name='delete_history'),
]