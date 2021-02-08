from django.urls import path
from .views import home, topics, new_topic, signup, topic_detail,reply_topic


urlpatterns = [

    path('', home, name='home'),
    path('topics/<id>', topics, name='topics'),
    path('topics/<id>/create_topic', new_topic, name='create_topic'),
    path('signup/', signup, name='signup'),
    path('topic_detail/<id>', topic_detail, name='topic_detail'),
    path('topic_detail/<id>/reply_topic', reply_topic , name='reply_topic')


]