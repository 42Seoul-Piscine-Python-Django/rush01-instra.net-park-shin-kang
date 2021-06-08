import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d42.settings")
application = get_wsgi_application()
application = WhiteNoise(application, root="")
application.add_files("/static/", prefix="")
application.add_files("/media/", prefix="")