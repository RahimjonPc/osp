from django.shortcuts import render, redirect
from .models import Foods
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin 
from .forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomsuccessMessageMixin:
    @property
    def success_msg(self):
        return False
    
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)
    
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)



class HomeDetailView(FormMixin,DetailView,CustomsuccessMessageMixin):
    model = Foods
    template_name = 'order.html'
    context_object_name =  'get_food'
    form_class = CommentForm
    success_msg = 'Comment Successfully added'
    
    def get_success_url(self,**kwargs):
        return reverse_lazy('order', kwargs={'pk':self.get_object().id})

    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.food = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)



def delete(request,pk):
    get_food = Foods.objects.get(pk=pk)
    get_food.delete()
    return redirect(reverse('create'))
