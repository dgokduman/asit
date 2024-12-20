import os
from django.core.wsgi import get_wsgi_application

# Doğru ayar modülünü belirtin: 'mysite.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
