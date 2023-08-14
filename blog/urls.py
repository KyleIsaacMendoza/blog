# blog/urls.py

# todo: we want to display our blog posts on the homepage so, as in the previous chapter, we'll first configure our django_project/urls.py file and then our app-level blog/urls.py file to achieve this.


from django.urls import path
from .views import BlogListView  # BlogListView is the CBV we created from blog/views.py

# new import from view the part 2
from .views import BlogDetailView
from .views import BlogCreateView  # new pt3
from .views import BlogUpdateView
from .views import BlogDeleteView


urlpatterns = [
    # for delete
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),  # edit
    path("post/new/", BlogCreateView.as_view(), name="post_new"),  # create
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),  # view
    path("", BlogListView.as_view(), name="home"),
]

# ? why the path is like that
# all blog post entries will start with post/
# next is the primary key for our post entry which will be represented as an integer, <int:pk>.


# next we can add the URL or link inside our empty link in templates
