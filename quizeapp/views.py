from django.shortcuts import render
from .models import Question, PnuUser, Answer
from django.core.paginator import Paginator
from rest_framework import pagination


def quiz_home(request): # 퀴즈 참여자가 호스트 메인 페이지에 들어올 때 user가 자동생성
    if request.GET:
        user = PnuUser()
        user.name = request.GET['name']
        if request.GET['name'] == "" :
            user.name = "익명"
        user.save()
        return redirect("quiz", user.pk)
    return render(request, 'quiz_home.html')


def quiz(request): # 퀴즈 띄우는 함수
    user = get_object_or_404(PnuUser, pk=pk) # 퀴즈 참여자
    real_ans = get_object_or_404(Answer) # 진짜 정답

    num = 1
    if request.POST: # 정답 채점 코드
        num = int(request.POST['quiz_id']) + 1 # num이 1 증가 (2, 3, ...)
        user.answer = user.answer + request.POST['answer'] # PnuUser의 answer 필드에 PnuUser가 제출한 답을 넣어줌
        if request.POST['answer'] == real_ans[num - 2]: # 정답 배열과 같으면 1점 플러스
            user.score += 1
            user.save()
        if num > 8:
            return redirect("ranking", pk)
        
    quiz = get_object_or_404(Question, id=num) # id값을 문제번호 num으로

    return render(request, "quiz.html", {'quiz':quiz})

def ranking(request, pk): # PnuUser 랭킹 매겨서 보여주는 함수
    user = get_object_or_404(PnuUser, pk = pk)
    all_user = PnuUser.objects.all()

    ranklist = all_user.order_by('score')
    # for i in all_user:
    #     each_user = i.name
    #     ranklist.append(each_user)
    # sorted(ranklist, reverse=True)

    return render(request, "ranking.html", {"'user' : user, 'ranklist' : ranklist"})

    


