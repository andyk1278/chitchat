"""chat/admin.py - register admin for models"""

from django.contrib import admin

from .models import ChatSession, ChatSessionMember, ChatSessionMessage


admin.site.register((ChatSession, ChatSessionMessage, ChatSessionMember))
