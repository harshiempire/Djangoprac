from django.urls import path, include
from . import views

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    path("signup/",views.SignUpAPIView.as_view(),name="signup")
]