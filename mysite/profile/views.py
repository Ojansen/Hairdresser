from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Profile, MyAccountManager
from .admin import UserCreationForm


class Register(generic.edit.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


class DetailView(generic.DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'
    login_url = 'login/'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     profile_search = Profile.objects.get(self.request.user)
    #     print(profile_search)
    #     return self.request.user

    def get(self, request, user):
        user = Profile.objects.get(pk=request.user.id)
        return render(request, 'profile/profile_detail.html', {'user': user})


class EditAccountView(generic.UpdateView):
    model = Profile
    template_name_suffix = '_edit'
    fields = ['first_name', 'last_name', 'email', 'address', 'mobile_nr']

    def post(self, request, pk):
        auth_user = get_object_or_404(Profile, pk=pk)
        try:
            profile = Profile.objects.get(pk=pk)
        except (KeyError, Profile.DoesNotExist):
            return render(request, 'profile/profile_edit.html', {
                'error_message': "You didn't select a choice.",
            })
        else:
            profile.first_name = request.POST['first_name']
            profile.last_name = request.POST['last_name']
            profile.email = request.POST['email']
            profile.address = request.POST['address']
            profile.mobile_nr = request.POST['mobile_nr']
            profile.save()
            print(profile)
            return HttpResponseRedirect(reverse('profile:profile-detail', args=(auth_user.id,)))


@require_http_methods(["POST"])
def profile_delete(request, pk):
    user = Profile.objects.get(pk=pk)
    if user.check_password(request.POST.get('password')):
        user.delete()
        return redirect('/')
    else:
        return render(request, 'profile/profile_detail.html', {'user': user})
