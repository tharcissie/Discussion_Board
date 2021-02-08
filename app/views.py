from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import *
from django.db.models import Count


# Create your views here.

def home(request):
    board = Board.objects.all()
    context={
        'board':board
    }
    return render(request, 'home.html', context)

def topics(request, id):
    board = get_object_or_404(Board, id=id)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts'))
    context={
        'board':board,
        'topics':topics
    }
    return render(request, 'topics.html', context)

@login_required(login_url='login')
def new_topic(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.author = request.user.profile
            topic.save()
            return redirect('topics', board.id)
    else:
        form = TopicForm()
    context={
        'board':board,
        'form':form
    }
    return render(request, 'create_topic.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def topic_detail(request, id):
    topic = get_object_or_404(Topic, id=id)
    topic.views += 1
    topic.save()
    context={
        'topic':topic
    }
    return render(request, 'topic_detail.html', context)

@login_required(login_url='login')
def reply_topic(request, id):
    topic = get_object_or_404(Topic, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user.profile
            post.save()
            return redirect('topic_detail', id=id)
    else:
        form = PostForm()
    return render(request, 'reply.html', {'topic': topic, 'form': form})


@login_required(login_url='login')
def profile(request, username):
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    context = {
        'prof_form': prof_form,
         }
    return render(request, 'profile.html', context)

def update_topic(request, id):
    topic = get_object_or_404(Topic, id=id)
    form = TopicForm(request.POST or None, instance = topic)
    if form.is_valid():
        form.save()
        return redirect('topic_detail', id=id)
    context={
        'form':form
    }
    return render(request, 'update_t.html', context)

    
def delete_topic(request, id):
    context ={} 
    topic = get_object_or_404(Topic, id = id) 
    if request.method =="POST": 
        topic.delete() 
        return redirect('home') 
  
    return render(request, "delete_t.html", context) 



