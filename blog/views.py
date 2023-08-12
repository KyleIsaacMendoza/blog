# blog/views.py

# todo: to create class based views to display the contents of our Post Model using ListView

# import
from django.views.generic import ListView  # 1st part

# todo:  after listView is done, (this is 2nd part) now we can add the functionality for the individual blog pages. We need to create a new VIEW, URL, and TEMPLATE.

from django.views.generic import DetailView  # new

from .models import Post  # import Post inside the blog/models.py


# Create your views here.
class BlogListView(ListView):
    model = Post  # put our database model Post inside model variable
    template_name = "home.html"


# todo: part 2 class for DetailView
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


# next is let's create templates.
# then add the templates folder inside the django_project/settings.py DIRS
