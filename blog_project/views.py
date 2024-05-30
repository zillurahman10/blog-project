from django.shortcuts import render
from posts.models import Post

def home(reuqeust):
    data = Post.objects.all()
    print(data)
    return render(reuqeust, 'home.html', {'data': data})