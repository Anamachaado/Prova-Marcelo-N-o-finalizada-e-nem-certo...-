from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    form = UsedCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'register.html', {'form':form})

def posts_view(request):
    posts = Post.objects.all().order_by('titulo')
    return render(request, 'post.html', {'posts: posts'})


