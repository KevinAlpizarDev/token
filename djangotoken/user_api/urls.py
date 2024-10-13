# from django.urls import path

# from .views import UserLogin, UserLogout, UserRegister, UserView

# urlpatterns = [
#     path("register", UserRegister.as_view(), name="register"),
#     path("login", UserLogin.as_view(), name="login"),
#     path("logout", UserLogout.as_view(), name="logout"),
#     path("user", UserView.as_view(), name="user"),
# ]

from django.urls import path

from . import views

urlpatterns = [
    path("register", views.UserRegister.as_view(), name="register"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),
    path("user", views.UserView.as_view(), name="user"),
]
