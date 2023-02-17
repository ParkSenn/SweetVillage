from django.db import models


class Answer(models.Model): # 점수를 매길 때 사용되는 진짜 정답들이 담김
    ans = models.CharField(default="", max_length=16, null=True, blank=True)


class Question(models.Model) : # 이용자에게 띄워줄 질문과 보기들이 담김
    question = models.CharField(max_length = 128)

    option_yes = models.CharField(max_length = 128)
    option_no = models.CharField(max_length = 128)

    def __str__(self):
        return self.question
    

class PnuUser(models.Model):
    name = models.CharField(max_length = 32, default = "익명")
    # quiz_url = modelsURLField(max_length=200, null=True, blank=True, unique=True)
    answer = models.CharField(max_length = 16)
    score = models.IntegerField(default = 0, null = True, blank = True)
    rank = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['score', 'name']