# Generated by Django 5.0.2 on 2024-05-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_student_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Nationality', models.CharField(max_length=20, unique=True)),
                ('Current_club', models.CharField(max_length=20, unique=True)),
                ('Date_of_Birth', models.DateField()),
                ('Total_games_played', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Total_goals', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Total_assists', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
