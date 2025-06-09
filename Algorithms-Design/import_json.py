import json
import os
import uuid
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

# تنظیمات جنگو
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Algorithms_Design.settings')
import django
django.setup()

from quize.models import CustomUser, Question, Answer

def load_json_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print("Error reading the JSON file. Please check the file structure.")
        return None

def create_users(data):
    for username, answers in data.items():
        if username == "Test for Bug":
            continue
        user, created = CustomUser.objects.get_or_create(
            username=username,
            defaults={
                'email': f"{username.lower()}@example.com",
                'name': username,
                'password': make_password('123456789'),
            }
        )
        if created:
            print(f"کاربر {username} ایجاد شد.")
        else:
            print(f"کاربر {username} از قبل وجود داشت.")

def create_questions(data):
    test_data = data.get("Test for Bug", [])
    for item in test_data:
        qnumber = item.get("qnumber")
        description = item.get("description", "")
        if not description or description == 0:
            description = f"Question {qnumber}"
        question, created = Question.objects.get_or_create(
            num_of_question=qnumber,
            defaults={
                'name': f"Q{qnumber}",
                'text': description,
                'all_questions': 3,
            }
        )
        if created:
            print(f"سوال {qnumber} ایجاد شد.")
        else:
            print(f"سوال {qnumber} از قبل وجود داشت.")

def create_answers(data):
    for username, answers in data.items():
        if username == "Test for Bug":
            continue
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            print(f"کاربر {username} یافت نشد.")
            continue

        for answer_data in answers:
            qnumber = answer_data.get("qnumber")
            description = answer_data.get("description")
            try:
                question = Question.objects.get(num_of_question=qnumber)
            except Question.DoesNotExist:
                print(f"سوال {qnumber} یافت نشد.")
                continue

            text_answer = description if description else None

            try:
                answer, created = Answer.objects.get_or_create(
                    user=user,
                    question=question,
                    defaults={
                        'text_answer': text_answer,
                    }
                )
                if created:
                    print(f"Answer for question {qnumber} has been created by {username}.")
                else:
                    print(f"Answer for question {qnumber} by {username} already existed.")
            except ValidationError as e:
                print(f"Error creating answer for {username} and question {qnumber}: {e}")

def import_json_to_db(json_file_path):
    data = load_json_data(json_file_path)
    if not data:
        return

    create_users(data)
    create_questions(data)
    create_answers(data)
    print("complete")

if __name__ == "__main__":
    json_file_path = "test.json"
    import_json_to_db(json_file_path)