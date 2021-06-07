from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from intranet.models import Comment, ReComment, Profile

class ProfileForm(forms.ModelForm):
    email=forms.EmailField(required=False)
    class Meta:
        model = Profile
        fields = ('image',)

class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


class ReCommentForm(forms.ModelForm):

    class Meta:
        model = ReComment
        fields = ('body','comment')
