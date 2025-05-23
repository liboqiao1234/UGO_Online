from django.urls import path

from message.views import MessageListView, MessageView, ReadAllMessageView, HasUnreadMessageView

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('<int:message_id>/', MessageView.as_view(), name='message_detail'),
    path('read_all/', ReadAllMessageView.as_view(), name='read_all'),
    path('has_unread/', HasUnreadMessageView.as_view(), name='has_unread'),
]
