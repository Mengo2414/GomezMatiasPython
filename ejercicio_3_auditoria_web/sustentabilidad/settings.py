import os\n"""Configuración mínima de Django para el panel de sustentabilidad."""

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
ROOT_URLCONF = "sustentabilidad.urls"
INSTALLED_APPS = ["django.contrib.staticfiles", "sustentabilidad"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    }
]
STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
