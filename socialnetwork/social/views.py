from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm
        context = {
            'post_list':posts,
            'form' : form,
        }

        return render(request, template_name='social/post_list.html', context=context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            context = {
                'post_list': posts,
                'form': form,
            }

            return render(request, template_name='social/post_list.html', context=context)