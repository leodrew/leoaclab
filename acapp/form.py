from django import forms
from django.contrib.auth.models import User
from acapp.models import Member,postBlog

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label='輸入密碼') ##密碼的欄位
    username = forms.CharField(label="輸入姓名")
    email = forms.CharField(label='電子信箱')
    class Meta():
        model = User
        fields = ('username','email','password')

class Memberform(forms.ModelForm):
    class Meta():
        model = Member
        fields = ('phone','job_title','id_card')
        
class PostblogForm(forms.ModelForm):
    class Meta():
        model = postBlog
        fields = ('authBlogId','blog_title','blog_content')