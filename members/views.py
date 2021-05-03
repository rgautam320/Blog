from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangedForm, ProfilePageCreateForm
from theblog.models import Profile
# Create your views here.


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'

    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangedForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html')


class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(
            *args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context['page_user'] = page_user
        return context


class EditProfilePage(UpdateView):

    model = Profile
    template_name = 'registration/edit_profile_page.html'
    form_class = ProfilePageCreateForm
    success_url = reverse_lazy('home')


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageCreateForm
    # fields = '__all__'
    template_name = 'registration/create_user_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')
