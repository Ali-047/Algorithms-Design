
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from algorithms import *
from models import *
from quizesecure.serializers import StudentSerializer, QuestionSerializer


# Create your views here.
class RegisterAPIView(APIView):
    serializer_class = None
    def post(self, request):
        data = request.data
        if not data:
            return Response({'error': 'No data provided'}, status=status.HTTP_400_BAD_REQUEST)
        if data['password'] != data['repeatPassword']:
            return Response({'error': 'رمز عبور و تکرار آن با هم برابر نیست'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class SignUpAPIView(RegisterAPIView):
    serializer_class = StudentSerializer


class QuizAPIView(APIView):
    final = None
    def put(self, request):
        data = request.data
        nationalID = request.data['nationalID']
        if not nationalID:
            return Response(data={"error": "nationalID is required"}, status=status.HTTP_400_BAD_REQUEST)
        answer = request.data['answer']
        try:
            user = Student.objects.get(nationalID=nationalID)
        except Student.DoesNotExist:
            return Response(data={"error": "student does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        if answer:
            if answer == self.final:
                data['is_draft'] = False
                serializer = QuestionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(status=status.HTTP_200_OK)



