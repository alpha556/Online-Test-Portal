from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exam(models.Model):
    exam_name = models.CharField(max_length=50)
    duration = models.DurationField()
    date_published = models.DateField('date published')

    def __str__(self):
        return self.exam_name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=100, verbose_name='option1', default='none')
    option2 = models.CharField(max_length=100, verbose_name='option2', default='none')
    option3 = models.CharField(max_length=100, verbose_name='option3', default='none')
    option4 = models.CharField(max_length=100, verbose_name='option4', default='none')
    answer = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(4), MinValueValidator(1)])

    def __str__(self):
        return 'Question:' + self.question_text


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return ' User :' + self.user.username + 'Exam :' + self.exam.exam_name + 'marks:' + str(self.marks)
