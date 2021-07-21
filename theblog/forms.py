from django import forms
from .models import Post, Profile, Comment, Category

# choices = [('Food', 'Food'), ('Travel', 'Travel')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'short_desc', 'header_image',
                  'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),

            'short_desc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),

            'header_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image Link'}),

            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),

            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),

            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog here...'}),
        }


class EditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'short_desc', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),

            'short_desc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),

            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog here...'}),
        }


class AddCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Category'}),
        }


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'value': 'Anonymous'}),

            'body': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }
