from django.db import models

# todo: create your models for your database
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # field for title
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    # field for author that has FK for many to one relationships
    # foreign key need to specify on_delete option

    body = models.TextField()  # field for blog of the author

    # ? def__str__
    # added to provide human-readable version of the model
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

        # ? this is for part 2 where we use DetailView because it expects either primary key or a slug passed to it as the identifier.

    # This tells Django how to calculate the canonical URL for our model Object. It says the URL named post_detail and pass in the PK.
