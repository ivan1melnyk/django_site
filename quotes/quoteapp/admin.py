from django.contrib import admin
from .models import Quote, Tag, Author

# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Quote)
