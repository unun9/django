from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, PasswordInput
import re


class RegisterForms(forms.Form):
    username = forms.CharField(max_length=100,
                               min_length=4,
                               required=True,
                               label='Введите имя ',
                               widget=TextInput(
                                   attrs={
                                       'placeholder': 'Логин',
                                       'class': 'form-control',
                                   }
                               ))
    email=forms.CharField(max_length=100,
                          label='Введите email ',
                          widget=TextInput(
                              attrs={
                                  'placeholder': 'email',
                                  'class': 'form-control',
                              }
                          ))

    password1 = forms.CharField(min_length=3, label="Пароль",
                                widget=PasswordInput(
                                    attrs={
                                        'class': 'form-control'
                                    }))
    password2 = forms.CharField(min_length=3, label="Повторите",
                                widget=PasswordInput(attrs={
                                    'class': 'form-control'
                                }))

    def clean_username(self):
        users = User.objects.filter(username=self.cleaned_data['username'])
        if users.count() > 0:
            raise ValidationError('ЭЭ Чувак данный юзер забронирован')
        return self.cleaned_data['username']

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError(' ЭЭ Чувак Пароли не совпадают')
        return self.cleaned_data['password2']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        user.save()
        return user


class loginForm(forms.Form):
    username = forms.CharField(max_length=100,
                               min_length=4,
                               required=True,
                               label='Введите Login ',
                               # regex='^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
                               widget=TextInput(
                                   attrs={
                                       'placeholder': 'Логин',
                                       'class': 'form-control',

                                   }
                               ))
    password1 = forms.CharField(min_length=3, label="Пароль",
                                widget=PasswordInput(
                                    attrs={
                                        'class': 'form-control'}))
