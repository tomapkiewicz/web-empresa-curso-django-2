from django.contrib import admin
from .models import Category, Post


# Register your models here.
class categoriesAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')


class postAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')
    list_display = ('title', 'author', 'published', 'post_categories')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    ordering = ('author', 'published')
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.shortdescription = "categorías"


admin.site.register(Category, categoriesAdmin)
admin.site.register(Post, postAdmin)
