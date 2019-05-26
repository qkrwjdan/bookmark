import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

    was_published_recently.admin_order_field = 'pub_date' #pub_date 로 정렬하겠다.
    was_published_recently.boolean = True #값이 불리언 값 형태인지 설정, True로 설정하면 값대신 아이콘이 나온다.
    was_published_recently.short_description = 'published recently?' #항목의 헤더 이름을 설정한다.

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
