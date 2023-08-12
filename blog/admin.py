# blog/admin.py
from django.contrib import admin

# todo: import Post that you created inside the models.py

from .models import Post

# Register your models here.

admin.site.register(Post)

# next step after adding post, or data inside the admin
# is to create the necessary views, URLS, and templates
# so we can display the information on our web application.
