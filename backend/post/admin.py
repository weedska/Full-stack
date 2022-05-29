from django.contrib import admin
from post.models import Post, Comment, Likes, Dislikes, CommentDislikes, CommentLikes

admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Dislikes)
admin.site.register(Comment)
admin.site.register(CommentDislikes)
admin.site.register(CommentLikes)
