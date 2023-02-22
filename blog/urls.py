"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentification.views
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
import blogs.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.login_page, name = 'login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('home/', blogs.views.home, name = 'home'),
    # path('', LoginView.as_view(template_name = "authentification/login.html", redirect_authenticated_user = True), name= 'login'),
    # path('', LogoutView.as_view(), name= "login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentification/password_change_form.html'),
         name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentification/password_change_done.html'), name='password_change_done'),
    path('profile-photo/upload/', authentification.views.upload_profile_photo,
         name='upload_profile_photo'),
    path('signup/', authentification.views.signup_page, name = 'signup'),
    path('photo/upload/', blogs.views.photo_upload, name='photo_upload'),
    path('blogs/create', blogs.views.blog_and_photo_upload, name='blog_create'),
    path('blogs/<int:blog_id>', blogs.views.view_blog, name = 'view_blog'), 
    path('blogs/<int:blog_id>/edit', blogs.views.edit_blog, name='edit_blog'),
    path('photo/upload_multiple/', blogs.views.create_multiple_photos, name = 'create_multiple_photos'), 
    path('follow-users/', blogs.views.follow_users, name='follow-users' ),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)