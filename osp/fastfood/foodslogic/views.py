from django.shortcuts import render, redirect
from .models import Comments
from foods.models import Foods
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin 
from foods.forms import CommentForm
from .forms import FoodsForm, AuthUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeListView(ListView):
    model = Foods
    template_name = 'index.html'
    context_object_name =  'list_food'


class CustomsuccessMessageMixin:
    @property
    def success_msg(self):
        return False
    
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)




class FoodCreateView(LoginRequiredMixin,CustomsuccessMessageMixin,CreateView):
    model = Foods
    template_name = 'create.html'
    form_class = FoodsForm
    success_url = reverse_lazy('create')
    success_msg = 'Successfully added'
    def get_context_data(self,**kwargs):
        kwargs['list_food'] = Foods.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class FoodEditView(LoginRequiredMixin,CustomsuccessMessageMixin,UpdateView):
    model = Foods
    template_name = 'create.html'
    form_class = FoodsForm
    success_url = reverse_lazy('create')
    success_msg = 'Successfully edited'
    def get_context_data(self,**kwargs):
        kwargs['edit'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs


class MyProjectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('create')
    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('create')
    success_msg = 'User successfully registered'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid


class MyProjectLogout(LogoutView):
    next_page = reverse_lazy('home')
