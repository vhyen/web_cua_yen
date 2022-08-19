from django.shortcuts import render
from .models import Post

from django.http import Http404

# Create your views here.
def list(request):
    Data = {'Post': Post.objects.all().order_by('-date')}
    #dictionary : 'Post' => name for the set of data (data tuple named as Post)
    return render(request, 'blog/blog.html', Data)

def post(request, pid):
    try:
        post_data = Post.objects.get(id = pid)
    except Post.DoesNotExist:
        raise Http404("The post does not exist.")
    return render(request, 'blog/post.html', {'post':post_data})

