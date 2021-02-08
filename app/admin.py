from django.contrib import admin
from .models import Board, Topic, Post, Profile

admin.site.register(Board)
admin.site.register(Profile)
admin.site.register(Topic)
admin.site.register(Post)
