from django.contrib import admin

from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category


# class PostInline(admin.TabularInline):
#     model = Post


class CategoryAdmin(admin.ModelAdmin):
    exclude = ["posts"]


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
