import os
from . import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
channel_layer = channels.asgi.get_channel_layer()
