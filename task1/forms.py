from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, label="Введите ваше имя:")
    password = forms.CharField(widget=forms.PasswordInput(), label="Введите ваш пароль:", min_length=8)
    repeat_password = forms.CharField(widget=forms.PasswordInput(), label="Повторите ваш пароль:", min_length=8)
    age = forms.IntegerField(label="Введите ваш возраст:")
