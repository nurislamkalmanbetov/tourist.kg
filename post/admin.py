from django.contrib import admin

from .models import Post, Comment, Category

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "created", "is_active"]
    list_filter = ["created", "author__username", "category", "is_active"] # author _ _ username - filtruet avtorov posta
                                                              #   list_filter dlya fitrasii postov i avtorov
    search_fields = ["title", "id", "text", "created"]#   поисковик всего в админке
    list_editable = ["category", "is_active"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "id"]
    prepopulated_fields = {"slug":("name",)}
