from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Comment, LikePost, Profile
from . models import   Post, Profile
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):

    post = Post.objects.all().order_by('-created_at')

    # profile = Profile.objects.get(user=request.user)
    #commenting --
    comments = Comment.objects.all()
    context = {
        'post': post,
       # 'profile': profile,
        'comments': comments,
    }
    return render(request, 'main.html',context)

def createPost(request):
    return render(request,'createPost.html')

def inProgress(request):
    return render(request,'inprogress.html')

def signup(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            emailid = request.POST.get('emailid')
            password = request.POST.get('password')
            my_user = User.objects.create_user(name,emailid,password)
            my_user.save()
            user_model = User.objects.get(username = name)
            new_profile = Profile.objects.create(user = user_model , id_user = user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request,my_user)
                return redirect('/home')
            return redirect('/loginn')
    except:
        invalid = "user already exists"
        return render(request, 'signup.html',{'invalid': invalid} )
    
    return render(request, 'signup.html')


def loginn(request):
 
  if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        print(name,password)
        userr=authenticate(request,username=name,password=password)
        if userr is not None:
            login(request,userr)
            return redirect('/home')
        
 
        invalid="Invalid Credentials"
        return render(request, 'loginn.html',{'invalid':invalid})
               
  return render(request, 'loginn.html')

def logoutt(request):
    logout(request)
    return redirect('/')

# def upload(request):

#     if request.method == 'POST':
#         user = request.user.username
#         audio = request.FILES.get('audio')
#         caption = request.POST['caption']

#         new_post = Post.objects.create(user=user, audio=audio, caption=caption)
#         new_post.save()

#         return redirect('/')
#     else:
#         return redirect('/')

from django.http import HttpResponseBadRequest

def upload(request):
    if request.method == 'POST':
        user = request.user.username
        audio = request.FILES.get('audio')
        video = request.FILES.get('video')
        caption = request.POST['caption']

        if audio:
            new_post = Post.objects.create(user=user, audio=audio, caption=caption)
        elif video:
            new_post = Post.objects.create(user=user, video=video, caption=caption)
        else:
            # Neither audio nor video file provided
            return HttpResponseBadRequest("Please provide either an audio or video file.")

        new_post.save()

        return redirect('/home')
    else:
        return redirect('/home')


def likes(request, id):
    if request.method == 'GET':
        username = request.user.username
        post = get_object_or_404(Post, id=id) 
        
        like_filter = LikePost.objects.filter(post_id = id, username = username).first()
        if like_filter is None :
            new_like = LikePost.objects.create(post_id = id , username = username)
            post.no_of_likes = post.no_of_likes + 1
        else:
            like_filter.delete()
            post.no_of_likes = post.no_of_likes - 1
        
        post.save()
        
        return redirect('/home')
        
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if request.method == 'POST':
        text = request.POST.get('text')
        new_comment = Comment.objects.create(post=post, user=user, text=text)
        new_comment.save()

    return redirect('/home')

def explore(request):
    post=Post.objects.all().order_by('-created_at')
    profile = Profile.objects.get(user=request.user)

    context={
        'post':post,
        'profile':profile
        
    }
    return render(request, 'explore.html',context)