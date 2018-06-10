""" chat/views.py - Views for the chat app."""
from django.http import Http404
from django.contrib.auth import get_user_model
from .models import (
        ChatSession, ChatSessionMember, ChatSessionMessage,
        deserialize_user
)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from notifications.signals import notify


class ChatSessionView(APIView):
    """Manage Chat sessions."""
    permission_class = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """create a new chat session."""
        user = request.user
        chat_session = ChatSession.objects.create(owner=user)
        return Response({
            'status': 'SUCCESS',
            'uri': chat_session.uri,
            'message': 'New chat session created.'
        })

    def patch(self, request, *args, **kwargs):
        """Add a user to a chat session."""
        user = get_user_model()
        uri = kwargs['wri']
        username = request.data['username']
        chat_session = ChatSession.objects.get(uri=uri)
        owner = chat_session.owner

        if owner != user:  # Onlyallow non owners join the room
            chat_session.members.get_or_create(
                user=user, chat_session=chat_session
            )

        owner = deserialize_user(owner)
        members = [
            deserialize_user(chat_session_user)
            for chat_session in chat_session.members.all()
        ]
        members.insert(0, owner)

        return Response({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined the chat' % user.username,
            'user': deserialize_user(user)
        })


class ChatSessionMessageView(APIView):
    """Create/Get Chat sessions messages."""
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *arg, **kwargs):
        """return all messages in a chat session."""
        uri = kwargs['uri']
        chat_session = ChatSession.objects.get(uri=uri)
        messages = [chat_session_message.to_json()
            for chat_session_message in chat_session.messages.all()]

        return Response({
            'id': chat_session.id, 'uri': chat_session.uri,
            'messages': messages
        })

    def post(self, request, *args, **kwargs):
        """create a new message in a chatsession."""
        uri = kwargs['uri']
        message = request.data['message']
        user = request.user
        chat_session = ChatSession.objects.get(uri=uri)

       chat_session_message = ChatSessionMessage.objects.create(
           user=user, chat_session=chat_session, message=message
        )

       notif_args = {
           'source': user,
           'source_diplay_name': user.get_full_name(),
           'category': 'chat', 'action': 'Sent',
           'obj': chat_session_message.id,
           'short_description': 'You a new message', 'silent': True,
           'extra_data': {
               'uri': chat_session.uri,
               'message': chat_session_message.to_json()
            }
        }

        notify.send(
           sender=self.__class__,**notif_args, channels=['websocket']
        )

        return Response({
            'status': 'SUCCESS', 'uri': chat_session.uri,
            'message': message, 'user': deserialize_user(user)
        })

def raise_404(request):
    """Raise a 404 error."""
    raise Http404
