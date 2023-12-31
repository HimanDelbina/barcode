# Generated by Django 4.0.4 on 2022-06-30 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('summary', models.TextField(help_text='Enter a brief description of the book', max_length=1000)),
                ('isbn', models.CharField(help_text='13 character', max_length=13, verbose_name='ISBN')),
                ('total_copies', models.IntegerField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='book_image')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter a book genre (e.g. Science Fiction,French poetry,Egnlish, German History etc)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the books's natural language (e.g. English,French,Jpaanese,etc.)", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=5)),
                ('contact_no', models.CharField(max_length=10)),
                ('total_book_due', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('pic', models.ImageField(blank=True, upload_to='profile_image')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(default='none', max_length=100)),
                ('rating', models.CharField(choices=[('0', '0'), ('.5', '.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5')], default=2, max_length=3)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('retrun_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Enter a brief description of the book', to='management.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.language'),
        ),
    ]
