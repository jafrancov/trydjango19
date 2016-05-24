from django.shortcuts import render

from .forms import UserLoginForm


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
    context = {
        'title': 'Login',
        'form': form,
    }
    return render(request, 'form.html', context)


def register_view(request):
    return render(request, 'form.html', {})


def logout_view(request):
    return render(request, 'form.html', {})

