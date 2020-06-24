from django.contrib import admin
from home.models import Contact
from home.models import Photo
from home.models import Post

# Register your models here.
admin.site.register(Contact)
admin.site.register(Photo)
admin.site.register(Post)