from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from .forms import CreatePostForm
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html',{'blogs':blogs})

def detail(request,blog_id):
    if blog_id==3:
        return render(request,'hidden.html')
        
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog_detail':blog_detail})

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            # blog = Blog()
            # blog.title = form.cleaned_data['title']
            # blog.body = form.cleaned_data['body']
            blog = form.save(commit=False)
            blog.pub_date = timezone.datetime.now()
            blog.save()
        return redirect('/detail/'+str(blog.id))
    else:
        form = CreatePostForm()
    return render(request,'create.html',{'form':form})

# def create_blog(request):
    # blog = Blog()
    # blog.title = request.GET['title']
    # blog.body = request.GET['body']
    # blog.pub_date = timezone.datetime.now()
    # blog.save()
    # return redirect('/detail/'+str(blog.id))

def update(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method =="POST":
        form = CreatePostForm(request.POST,request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
            return redirect('/detail/'+str(blog_id))
    else:
        form = CreatePostForm(instance=blog)
        return render(request, 'create.html',{'form':form})

def delete(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('home')