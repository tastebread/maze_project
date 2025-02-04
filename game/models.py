from django.db import models
from django.contrib.auth.models import User

class Puzzle(models.Model): #문제(제목,질문,힌트,정답 다음문제) 저장
    title = models.CharField(max_length=200)
    question = models.TextField()
    answer = models.CharField(max_length=100)
    hint = models.TextField(blank=True, null=True)
    next_puzzle = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class PlayerProgress(models.Model): # 사용자의 현재 진행사항 저장
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_puzzle = models.ForeignKey(Puzzle, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0)