from .settings import * 

#Settings for tests to use memory for database and prevent email being sent
DATABASES = {
    #Settings for tests to use memory for database and prevent email being sent
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
