from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

from .text_similatry import *


# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data

        try:
            name = data.get('name')
            username = data.get('username')
            password = data.get('password')
            repeat_password = data.get('repeatPassword')
            is_company = data.get('is_company')
        except KeyError as e:
            return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        if not name:
            return Response({'error': 'name is missing'}, status=status.HTTP_400_BAD_REQUEST)
        if not username:
            return Response({'error': 'username is missing'}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'error': 'password is missing'}, status=status.HTTP_400_BAD_REQUEST)
        if not is_company:
            return Response({'error': 'is_company is missing'}, status=status.HTTP_400_BAD_REQUEST)
        if password != repeat_password:
            return Response({'error': 'رمز عبور و تکرار آن با هم برابر نیست'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if CustomUser.objects.filter(username=username).exists():
                return Response({'error': 'نام کاربری قبلاً استفاده شده است'}, status=status.HTTP_400_BAD_REQUEST)

            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                name=name,
                is_company=is_company
            )
            user_serializer = UserSerializer(user)
        except IntegrityError:
            return Response({'error': 'نام کاربری قبلاً استفاده شده است'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'خطا در ایجاد کاربر: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user_id = request.query_params.get('id')
        if not user_id:
            return Response(data={"error": "User ID missing"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(data={"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user_serializer = UserSerializer(instance=user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user_id = request.data.get('id')
        if not user_id:
            return Response(data={"error": "User ID missing"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(data={"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            print('serializer validated')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StartQuestionnaireView(APIView):
    def get(self, request):
        first_question = Question.objects.get(id=1)
        if not first_question:
            return Response({"error": "No questions available"}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={"question": QuestionSerializer(first_question).data}, status=status.HTTP_200_OK)


class SubmitAnswerView(APIView):
    def post(self, request):
        username = request.data.get('username')
        if not username:
            return Response(data={'error': 'nationalID missing'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(username=username)
        except ObjectDoesNotExist:
            return Response(data={'error': 'user with this student code does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

        question_name = request.data.get('question')
        if not question_name:
            return Response(data={'error': 'question missing'}, status=status.HTTP_400_BAD_REQUEST)

        question = get_object_or_404(Question, name=question_name)

        text_answer = request.data.get('text_answer')
        if not text_answer:
            return Response(data={'error': 'text_answer missing for open-ended question'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            answer = Answer(
                question=question,
                text_answer=text_answer
            )
            answer.user.add(user)
            answer.save()
        except ValidationError as e:
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error saving answer: {str(e)}")
            return Response(data={'error': f'Failed to save answer: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        questionid = question.id
        questionid += 1
        next_question = Question.objects.get(
            id__gt=questionid
        )

        if not next_question:
            return Response({"message": "Questionnaire completed"}, status=status.HTTP_202_ACCEPTED)

        return Response(data={'question': QuestionSerializer(next_question).data}, status=status.HTTP_200_OK)
