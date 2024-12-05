from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, "تم تسجيل حساب جديد بنجاح")
        return redirect('login')
    form = SignUpForm()
    return render(request, "usermodule/register.html", {"form": form})

def loginUser(request):
    if request.session.get('loggedIn') != True:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                messages.success(request, "تم تسجيل الدخول بنجاح")
                request.session['loggedIn'] = True
                return redirect('/books')
        else:
            form = LoginForm()
        return render(request, 'usermodule/login.html', {'form': form})
    else:
        return redirect('/books')

def logoutUser(request):
    if request.session.get('loggedIn'):
        del request.session['loggedIn']
        messages.success(request, "تم تسجيل الخروج بنجاح")
    else:
        messages.error(request, "لم تسجل الدخول حتى تسجل خروج!")

    return redirect('/books')
