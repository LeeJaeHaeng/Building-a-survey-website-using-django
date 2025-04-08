from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.SurveyListView.as_view(), name='index'),
    path('<int:pk>/', views.SurveyDetailView.as_view(), name='detail'),
    path('<int:survey_id>/response/', views.survey_response, name='survey_response'),
    path('<int:survey_id>/response/<int:response_id>/', views.answer_questions, name='answer_questions'),
    path('<int:survey_id>/complete/', views.survey_complete, name='survey_complete'),
]