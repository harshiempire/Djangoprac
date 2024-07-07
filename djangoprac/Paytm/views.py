from django.shortcuts import render, redirect
from .forms import SignupForm
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpAPIView(APIView):
    def post(self,request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            return Response({
                "message": "User created successfully",
                "token": "Bearer "+str(token)
            })
        return Response(serializer.errors)

class SignInAPIView(APIView):
    def post(self,request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        if not username or not password :
            return Response({
                "message": "Error while logging in",
            })
    

    
# # Create your views here.
# def signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'form': form})
#         else:
#             errors = form.errors.as_json()
#             return JsonResponse({'errors': errors})
#     else:
#         print("hellohi")
#         form = SignupForm()
#     return render(request, 'Paytm/signup.html', {'form': form})
