# Generated by Django 5.2 on 2025-04-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_question_type_questionchoice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='selected_choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='정답 여부'),
        ),
        migrations.AddField(
            model_name='question',
            name='choice_options',
            field=models.TextField(blank=True, help_text='객관식 선택지를 줄바꿈으로 구분하여 입력하세요. 정답은 앞에 *를 붙여주세요.', verbose_name='객관식 선택지'),
        ),
        migrations.DeleteModel(
            name='QuestionChoice',
        ),
    ]
