# Generated by Django 4.2.2 on 2023-10-01 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0003_remove_reviews_book_remove_reviews_student_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Book",
            new_name="BarCodeModel",
        ),
    ]
