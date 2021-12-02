from django.shortcuts import render, redirect
from .forms import (
    UserRegistration,
    UserUpdateForm,
    ProfileUpdateForm,

)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Post, Disease, Herb


# Create your views here.
# ---------------------------Start-------------Create--Views---------------start---------------------#
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DiseaseCreateView(LoginRequiredMixin, CreateView):
    model = Disease
    fields = ['DiseaseName', 'DiseaseDescription', 'status', 'DiseasePhoto']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HerbCreateView(LoginRequiredMixin, CreateView):
    model = Herb
    fields = ['HerbName', 'diseaseName', 'HerbPhoto']
    success_url = reverse_lazy('herb_detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# --------------------------------end--------Create--Views----------------end--------------------#
# ---------------------------start-------------ListViews---------------start---------------------#


class PostListView(ListView):
    model = Post
    template_name = 'myapp/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class DiseaseListView(ListView):
    model = Disease
    template_name = 'myapp/diseases.html'
    context_object_name = 'diseases'
    ordering = ['-date_posted']


class HerbListView(ListView):
    model = Herb
    template_name = 'myapp/herb.html'
    context_object_name = 'herbs'
    ordering = ['-date_posted']
# -------------------------end---------------ListViews-------------------end-----------------#
# -------------------------start---------------DetailView-------------------start-----------------#


class PostDetailView(DetailView):
    model = Post
    template_name = 'myapp/detail_view.html'


class DiseaseDetailView(DetailView):
    model = Disease
    template_name = 'myapp/disease_detail.html'


class HerbDetailView(DetailView):
    model = Herb
    template_name = 'myapp/herb_detail.html'
# -------------------------end---------------DetailView-------------------end-----------------#
# -------------------------start---------------UpdateView-------------------start-----------------#


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        mypost = self.get_object()
        if self.request.user == mypost.author:
            return True
        return False


class DiseaseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Disease
    fields = ['DiseaseName', 'DiseaseDescription', 'status', 'DiseasePhoto']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        mypost = self.get_object()
        if self.request.user == mypost.author:
            return True
        return False


class HerbUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Herb
    fields = ['HerbName', 'diseaseName', 'HerbPhoto']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        mypost = self.get_object()
        if self.request.user == mypost.author:
            return True
        return False
# -------------------------end---------------UpdateView-------------------end-----------------#
# -------------------------start---------------DeleteView-------------------start-----------------#


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        mypost = self.get_object()
        if self.request.user == mypost.author:
            return True
        return False


class DiseaseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Disease
    success_url = reverse_lazy('disease')

    def test_func(self):
        mypost = self.get_object()
        if self.request.user == mypost.author:
            return True
        return False
# -------------------------start---------------DeleteView-------------------start-----------------#


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'myapp/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegistration()
    return render(request, 'register.html', {'form': form})


def post(request):
    return render(request, 'myapp/post.html')
