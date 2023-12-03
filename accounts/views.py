from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm
from polls.models import Quiz, UserAnswer
from django.utils import timezone
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import UserProfile
from polls.views import completed
@login_required(login_url=None)
def custom_logout(request):
    logout(request)
    return redirect('/')

def register(request):

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.is_staff = False
            new_user.save()

            profile, created = UserProfile.objects.get_or_create(user=new_user)
            profile.name = user_form.cleaned_data['name']
            profile.birthdate = user_form.cleaned_data['birthdate']
            profile.gender = user_form.cleaned_data['gender']
            profile.is_special_user = user_form.cleaned_data['is_special_user']

            if not user_form.cleaned_data['is_special_user']:
                selected_users = user_form.cleaned_data['selected_user']
                profile.selected_users.set([selected_users])
            else:
                profile.selected_users.clear()

            profile.save()

            latest_quiz_list = Quiz.objects.all()
            for quiz in latest_quiz_list:
                # UserAnswer에 새로운 레코드 추가
                user_answer = UserAnswer.objects.create(
                    user=new_user,
                    quiz=quiz,
                    selected_answer=None,
                    is_correct=False,
                    image=None,
                    date_answered=timezone.now(),
                    score=0
                )

            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html',{'form':user_form})

def user_list(request):
    current_user_profile = UserProfile.objects.get(user=request.user)
    is_special_user = current_user_profile.is_special_user

    if is_special_user:
        users = UserProfile.objects.filter(is_special_user=False)
        return render(request, 'registration/user_list.html', {'users': users})
    else:
        # 특별 사용자가 아닌 경우 처리 (원하는 방법에 따라 구현)
        return render(request, 'registration/profile.html')

@login_required
def select_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            selected_user = form.cleaned_data['selected_user']
            return redirect('user_profile', user_id=selected_user.id)
    else:
        form = RegisterForm()

    return render(request, 'registration/select_user.html', {'form': form})
@login_required
def user_profile(request, user_id):
    # 특별 사용자인지 확인합니다
    current_user_profile = UserProfile.objects.get(user=request.user)
    is_special_user = current_user_profile.is_special_user

    # 선택된 사용자 정보를 가져옵니다
    selected_user = get_object_or_404(User, id=user_id)

    try:
        profile = UserProfile.objects.get(user=selected_user)
        user_answers = UserAnswer.objects.filter(user=selected_user)
        total_score = user_answers.aggregate(Sum('score'))['score__sum']

    except UserProfile.DoesNotExist:
        profile = None
        user_answers = []
        total_score = 0

    return render(
        request,
        'registration/user_profile.html',
        {
            'user_profile': profile,
            'total_score': total_score,
            'user_answers': user_answers,
            'is_special_user': is_special_user,
        }
    )