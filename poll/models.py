from django.db import models


class Question(models.Model):
    question_text = models.CharField(verbose_name='Pergunta', max_length=200)
    published = models.BooleanField(
        verbose_name='Publicar?',
        help_text='Se o campo estiver marcado a enquete será publicada imediatamente.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name='Resposta', max_length=200)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice_text
