# Generated by Django 5.1 on 2024-08-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0005_rename_associted_habit_habit_associated_habit_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.DurationField(
                blank=True,
                help_text="Укажите периодичность выполнения привычки для напоминания в днях (по умолчанию ежедневная)",
                null=True,
                verbose_name="Периодичность",
            ),
        ),
    ]
