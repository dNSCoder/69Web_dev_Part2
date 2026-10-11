from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email =forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","first_name","last_name", "email", "password1", "password2")

    def __init__(self, *args, **kwagrs):
        super().__init__(*args, **kwagrs) #เรียก init เดิมของ superClass ==> UsercreationForm
        for field in self.fields.values(): #ใช้ css เข้ามาประกอบ
            field.widget.attrs.update({"class": "form-control"})

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]

    def __init__(self, *args, **kwagrs):
            super().__init__(*args, **kwagrs)
            for field in self.fields.values(): 
                field.widget.attrs.update({"class": "form-control"})