from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from . import forms
from django.conf import settings
# Create your views here.



def login_page(request):
   form = forms.LoginForm()
   message = ''
   if request.method == 'POST':
       form = forms.LoginForm(request.POST)
       
       if form.is_valid():
           user = authenticate(
			   username = form.cleaned_data["username"],
			   password = form.cleaned_data["password"],
		   ) 
           if user is not None:
               login(request, user)
               return redirect('home')
           else:
               message ='identifiant invalide'
               
   return render(request, 'authentification/login.html', context={'form': form, 'message': message})

def logout_user(request):
    
    logout(request)
    return redirect('login')

# class LogoutPageView(View):
#     template_name = 'authentification/login.html'
    
#     def logout(request):
#         return redirect('template_name')
        
        
    

# class LoginPageView(View):
    
#     template_name = 'authentification/login.html'
#     form_class = forms.LoginForm
    
#     def get(self,request):
        
#         form = self.form_class()
#         message = ''
        
#         return render(request, self.template_name, {'form': form, 'message': message})
    
#     def post(self, request):
        
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username = form.cleaned_data['username'],
#                 password = form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect ('home')
#             message = 'echec indentification'
#         return render(request, self.template_name, context={'form': form, 'message': message})

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
               login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/signup.html', context = {'form': form}) 
            
        
    
# def upload_profile_photo(request):
#     form = forms.UploadProfilePhotoForm(instance=request.user)
#     if request.method == 'POST':
#         form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
            
#             user =  form.save()
#             login(request, user)
#             return redirect('home')
#         return render(request, 'authentification/upload_profile_photo.html', context = {'form': form}) 

def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance= request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentification/upload_profile_photo.html', context={'form': form})