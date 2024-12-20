import os
from django.core.wsgi import get_wsgi_application

# Doğru ayar modülünü belirtin: 'start.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'start.settings')

application = get_wsgi_application()
