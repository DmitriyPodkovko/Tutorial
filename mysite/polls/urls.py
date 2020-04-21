from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /polls/question/
    path('question/', views.QuestionList.as_view(), name='list'),
    # ex: /polls/question/5/
    path('question/<int:question_id>/', views.QuestionDetail.as_view(), name='detail'),
    # ex: /polls/choice/
    path('choice/', views.ChoiceList.as_view(), name='list'),
    # ex: /polls/choice/5/
    path('choice/<int:choice_id>/', views.ChoiceDetail.as_view(), name='detail'),
]
