from django.contrib import admin

from posts.models import Group, Post, Follow, Comment


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'image', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    list_editable = ('group',)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'created')


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Comment, CommentAdmin)
