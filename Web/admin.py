from django.contrib import admin
import models

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','hidden','publish_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','parent_comment','comment','date')


admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.ThumbUp)
admin.site.register(models.user_profile)
admin.site.register(models.user_group)
