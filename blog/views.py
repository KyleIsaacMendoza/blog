# blog/views.py

# todo: to create class based views to display the contents of our Post Model using ListView

# import
from django.views.generic import ListView  # 1st part

# todo:  after listView is done, (this is 2nd part) now we can add the functionality for the individual blog pages. We need to create a new VIEW, URL, and TEMPLATE.

from django.views.generic import DetailView  # new
from django.views.generic.edit import CreateView  # new for creating view

from django.views.generic.edit import UpdateView  # new for updating

from django.views.generic.edit import DeleteView  # new for deleting.
from django.urls import reverse_lazy  # new


from .models import Post  # import Post inside the blog/models.py


# Create your views here.
class BlogListView(ListView):
    model = Post  # put our database model Post inside model variable
    template_name = "home.html"


# todo: part 2 class for DetailView
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


# todo: part3 class for CreateView
class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]
    # next step is to create a template (form) for CreateView class to use


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

    # let's assume that title and body is the thing we need to change and not the author thats why we didnt past the author in the fields.


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    # reverse_lazy(viewname, urlconf=none, args=none...) here as opposed to just reverse so that it won't execute the URL redirect until our view has finished deleting the blog post.


# next is let's create templates.
# then add the templates folder inside the django_project/settings.py DIRS
