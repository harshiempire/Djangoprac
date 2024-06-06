from django.shortcuts import render

# Create your views here.
def app_in_dj(request):
    return render(request,"appindj/app_in_dj.html")