from django.shortcuts import render,get_object_or_404
from django.views import generic
# from django.views.generic import *
#from django.views.generic.edit import CreateView
from .models import *
from .forms import *

class PostList(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    # context_object_name = 'post'
    # queryset = Post.objects.filter(status=1).order_by('-created_on')

def home(request):
	slides = Slider.objects.all() 
	return render(request,'home.html',{'slides':slides})


def PostDetail(request, slug): 
    post = get_object_or_404(Post, slug=slug)
    return render(request, "post_detail.html", {'post':post}) 

# class BookListView(generic.ListView):
#     model = Book
#     context_object_name = 'my_book_list'   # your own name for the list as a template variable
#     queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
#     template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save() # saves in database
			messages.success(request, f"Your message has been sent.Thanks for visiting our site!")
	else:
		form = ContactForm()
	return render(request,'contact.html',{'form': form})

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
