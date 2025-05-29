from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data.get('name'),
        )
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.is_company = validated_data.get('is_company', instance.is_company)
        instance.name = validated_data.get('name', instance.name)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    question_type = serializers.CharField()

    class Meta:
        model = Question
        fields = ['name', 'text', 'num_of_question', 'all_questions']



class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    text_answer = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = Answer
        fields = ['question','text_answer']


