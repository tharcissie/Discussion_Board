from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.jpg')

    def __str__(self):
         return self.user.username

    @receiver(post_save, sender=User)
    def save_user(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def delete_user(self):
        self.delete()


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=4000, default="")
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE, related_name='topics')
    author = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='topics')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.name

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
