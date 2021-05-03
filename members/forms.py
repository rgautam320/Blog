from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    last_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget.attrs['class'] = 'form-control'

        self.fields['password2'].widget.attrs['class'] = 'form-control'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class EditProfileForm(UserChangeForm):

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    username = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    first_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    last_name = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email')


class PasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Old Password', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'New Password', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm New Password', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfilePageCreateForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = ('bio', 'job_title', 'phone', 'profile_picture', 'website_URL', 'facebook_URL',
                  'instagram_URL', 'twitter_URL', 'youtube_URL', 'github_URL', 'linkedin_URL')

        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),

            'job_title': forms.TextInput(attrs={'class': 'form-control'}),

            'phone': forms.TextInput(attrs={'class': 'form-control'}),

            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),

            'website_URL': forms.TextInput(attrs={'class': 'form-control'}),

            'facebook_URL': forms.TextInput(attrs={'class': 'form-control'}),

            'twitter_URL': forms.TextInput(attrs={'class': 'form-control'}),

            'instagram_URL': forms.TextInput(attrs={'class': 'form-control'}),

            'youtube_URL': forms.TextInput(attrs={'class': 'form-control'}),

            'github_URL': forms.TextInput(attrs={'class': 'form-control'}),

            'linkedin_URL': forms.TextInput(attrs={'class': 'form-control'}),
        }
