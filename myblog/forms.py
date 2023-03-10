from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Placeholder'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Placeholder'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type your content here..'})
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Placeholder'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title Placeholder'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type your content here..'})
        }
