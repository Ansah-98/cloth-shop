from django.contrib import admin

# Register your models here
from .models import Product,Profile,Comment


admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Comment)