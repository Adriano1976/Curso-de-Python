import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Questionário(s)')
    pub_date = models.DateTimeField('Data de Publicação')

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='publicado recentemente?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Questão')
    choice_text = models.CharField(max_length=200, verbose_name='Opção')
    votes = models.IntegerField(default=0, verbose_name='Votos')

    def __str__(self):
        return self.choice_text
