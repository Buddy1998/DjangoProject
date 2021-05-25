

from django.shortcuts import render,redirect
from .models import log,Post
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.views import View
from django.http import HttpResponseRedirect

def home(request):
    log1=log.objects.all()
    return render(request,"home.html")              # the moment it is called send response
                                                                    # name is in dictonary format  JSON format
def inside(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            username= request.user.username
            post_text = request.POST['post_text']
            data = log()
            data.name = username
            data.text = post_text
            data.save()
        return redirect('allposts2')
    else:
         return render(request,"inside.html")

def allposts2(request):
    all_text = log.objects.all()
    return render(request,"allposts2.html",{'all_text':all_text})


#
# def like(request):
#
#     if request.method == 'GET':
#         post_id = request.GET['post_id']
#         like=likeapp()
#         like.post_id=post_id
#         like.likes=like.likes+1
#
#         like.save()
#         return HttpResponse(post_id,{'likes':like.likes})
#     else:
#         return HttpResponse("Request method is not a GET")
#
# def dislike(request):
#
#     if request.method == 'GET':
#         post_id = request.GET['post_id']
#         dislike=likeapp()
#         dislike.post_id=post_id
#
#         dislike.save()
#         return HttpResponse(post_id)
#     else:
#         return HttpResponse("Request method is not a GET")

class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)
        next=request.POST.get('next','/')
        return HttpResponseRedirect(next)

class AddDislike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next=request.POST.get('next','/')
        return HttpResponseRedirect(next)

