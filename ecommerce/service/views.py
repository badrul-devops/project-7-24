from django.shortcuts import render
from .form import UserForm
from .models import User

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_portal')
    else:
        form = UserForm()
    
    return render(request, 'user_form.html', {'form': form})

def admin_portal(request):
    users = User.objects.all()
    return render(request, 'admin_portal.html', {'users': users})


def home(request):
    return render(request, 'home.html')
def userlogin(request):
    return render(request, 'user_login.html')
def userregister(request):
    return render(request, 'registation.html')