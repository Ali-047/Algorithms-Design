import json
import os
import uuid
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

# تنظیمات جنگو
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Algorithms_Design.settings')  # نام پروژه با خط تیره
import django
django.setup()

# حالا مدل‌ها رو وارد می‌کنیم
from quize.models import CustomUser, Question, Answer

def load_json_data(file_path):
    """خواندن فایل JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"فایل {file_path} یافت نشد.")
        return None
    except json.JSONDecodeError:
        print("خطا در خواندن فایل JSON. لطفاً ساختار فایل را بررسی کنید.")
        return None

def create_users(data):
    """ایجاد کاربران از داده‌های JSON"""
    for username, answers in data.items():
        if username == "Test for Bug":
            continue  # این کلید برای سوالاته، نه کاربر
        user, created = CustomUser.objects.get_or_create(
            username=username,
            defaults={
                'email': f"{username.lower()}@example.com",
                'name': username,
                'password': make_password('defaultpassword123'),  # رمز پیش‌فرض
            }
        )
        if created:
            print(f"کاربر {username} ایجاد شد.")
        else:
            print(f"کاربر {username} از قبل وجود داشت.")

def create_questions(data):
    """ایجاد سوالات از کلید 'Test for Bug'"""
    test_data = data.get("Test for Bug", [])
    for item in test_data:
        qnumber = item.get("qnumber")
        description = item.get("description", "")
        # اگر description خالی یا null یا 0 باشه، یه متن پیش‌فرض می‌ذاریم
        if not description or description == 0:
            description = f"Question {qnumber}"
        question, created = Question.objects.get_or_create(
            num_of_question=qnumber,
            defaults={
                'name': f"Q{qnumber}",
                'text': description,
                'all_questions': 3,  # تعداد کل سوالات (ثابت)
            }
        )
        if created:
            print(f"سوال {qnumber} ایجاد شد.")
        else:
            print(f"سوال {qnumber} از قبل وجود داشت.")

def create_answers(data):
    """ایجاد پاسخ‌ها برای هر کاربر"""
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

            # اگر description خالی یا null باشه، None می‌ذاریم
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
                    print(f"پاسخ برای سوال {qnumber} توسط {username} ایجاد شد.")
                else:
                    print(f"پاسخ برای سوال {qnumber} توسط {username} از قبل وجود داشت.")
            except ValidationError as e:
                print(f"خطا در ایجاد پاسخ برای {username} و سوال {qnumber}: {e}")

def import_json_to_db(json_file_path):
    """تابع اصلی برای وارد کردن داده‌های JSON به دیتابیس"""
    data = load_json_data(json_file_path)
    if not data:
        return

    # ایجاد کاربران
    create_users(data)
    # ایجاد سوالات
    create_questions(data)
    # ایجاد پاسخ‌ها
    create_answers(data)
    print("وارد کردن داده‌ها به دیتابیس با موفقیت انجام شد.")

if __name__ == "__main__":
    json_file_path = "test.json"  # مسیر فایل JSON
    import_json_to_db(json_file_path)