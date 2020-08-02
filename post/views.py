from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import Postform

# Create your views here.
def main(request):
    blog=Post.objects.all().order_by('-id')
    return render(request, 'main.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def detail(request, blog_id):
    blog=get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog})

def renew(request, blog_id):
    blog=get_object_or_404(Post, pk=blog_id)
    return render(request, 'renew.html', {'blog':blog})

def create(request):
    blog=Post()
    blog.title=request.POST['title']
    try:
        blog.image=request.FILES['image']
    except:
        pass
    blog.body=request.POST['body']
    blog.save()
    return redirect('/detail/' + str(blog.id))

def update(request, blog_id):
    blog=get_object_or_404(Post, pk = blog_id)
    blog.title=request.POST['title']
    try:
        blog.image=request.FILES['image']
    except:
        pass
    blog.body=request.POST['body']
    blog.save()
    return redirect('/detail/' + str(blog.id))

def delete(request, blog_id):
    blog=get_object_or_404(Post, pk=blog_id)
    blog.delete()
    return redirect('/')

def newform(request):
    if request.method == "POST":
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Postform()
        return render(request, 'newform.html', {'form':form})

def updateform(request, blog_id):
    form_u = get_object_or_404(Postform, pk=blog_id)

    if request.method == "POST":
        form = Postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=Postform(instance=form_u)
        return render(request, 'updateform.html', {'form':form})
