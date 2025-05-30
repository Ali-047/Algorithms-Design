from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *


urlpatterns = [
    path('register/',RegisterAPIView.as_view(),name = 'sign up'),
    path('start/questionnaire/',StartQuestionnaireView.as_view(),name = 'StartQuestionnaire'),
    path('submit/answer/',SubmitAnswerView.as_view(),name = 'submitAnswer'),
    path('similarity/', SimilarityAPIView.as_view(),name = 'similarity'),
]