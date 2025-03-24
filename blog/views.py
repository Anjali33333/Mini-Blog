from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Profile, Comment
from .forms import PostForm, ProfileUpdateForm, CommentForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.urls import reverse

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('user_posts', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'blog/profile_update.html', {'form': form})

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted'),
        'total_posts': Post.objects.count(),
        'published_posts': Post.objects.count()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.count()
        context['published_posts'] = Post.objects.count()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        context['comment_form'] = CommentForm()
        context['is_liked'] = post.likes.filter(id=self.request.user.id).exists()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog-home')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse('blog-home')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse('blog-home')

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def like_post(request, pk):
    if request.method == 'POST' and request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        return JsonResponse({
            'liked': liked,
            'total_likes': post.total_likes()
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

def like_comment(request, pk):
    if request.method == 'POST' and request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)
        if comment.likes.filter(id=request.user.id).exists():
            comment.likes.remove(request.user)
            liked = False
        else:
            comment.likes.add(request.user)
            liked = True
        return JsonResponse({
            'liked': liked,
            'total_likes': comment.total_likes()
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

def add_comment(request, pk):
    if request.method == 'POST' and request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)
