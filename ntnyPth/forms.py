from django import forms

from ntnyPth.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post_info']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment_info']
