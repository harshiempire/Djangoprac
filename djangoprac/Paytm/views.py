from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print("hi")
            form.save()

        else:
            print("hello")
            return render(request, 'Paytm/signup.html', {'form': form})
    else:
        print("hellohi")
        form = SignupForm()
    return render(request, 'Paytm/signup.html', {'form': form})