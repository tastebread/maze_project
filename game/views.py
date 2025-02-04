from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("puzzle")  # 가입 후 미궁 게임으로 이동
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})

from .models import Puzzle, PlayerProgress
from django.contrib.auth.decorators import login_required

@login_required
def puzzle_view(request):
    progress, created = PlayerProgress.objects.get_or_create(user=request.user, defaults={"current_puzzle": Puzzle.objects.first()})
    puzzle = progress.current_puzzle

    if request.method == "POST":
        user_answer = request.POST.get("answer", "").strip().lower()
        if user_answer == puzzle.answer.lower():
            progress.current_puzzle = puzzle.next_puzzle
            progress.score += 10  # 정답 맞추면 점수 증가
            progress.save()
            return redirect("puzzle")
    
    return render(request, "puzzle.html", {"puzzle": puzzle})