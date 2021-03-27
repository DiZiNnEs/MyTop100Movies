import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'own_selection_top_films.settings')

application = get_wsgi_application()
