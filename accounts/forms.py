from django.contrib.auth.models import User
from django import forms
from .models import UserProfile
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput)
    #selected_user = forms.ModelChoiceField(queryset=User.objects.all(), label='Select a user')
    name = forms.CharField(max_length=255, required=False, label='이름')
    birthdate = forms.DateField(required=False, label='생년월일')
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=False,label='성별')
    is_special_user = forms.BooleanField(initial=False, required=False, label='특별 사용자로 지정')
    selected_user = forms.ModelChoiceField(queryset=User.objects.all(), label='Select a user', required=False)


    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'name', 'birthdate', 'gender', 'is_special_user', 'selected_user' ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('패스워드가 옳지 않습니다.')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.name = self.cleaned_data['name']
            profile.birthdate = self.cleaned_data['birthdate']
            profile.gender = self.cleaned_data['gender']
            profile.is_special_user = self.cleaned_data['is_special_user']

            if self.cleaned_data['is_special_user']:
                # Assuming 'selected_user' is a ForeignKey to another User model
                profile.special_users.set([self.cleaned_data.get('selected_user')])
            else:
                # Clear special_users for regular users
                profile.special_users.clear()
            profile.save()

        return user