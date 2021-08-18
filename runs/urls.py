from django.urls import path
from . import views

app_name = 'runs'

urlpatterns = [
    path('', views.all_runs, name='all_runs'),
    path('<int:run_id>/', views.detail, name='detail'),
]
