from .celery import app as celery_app
__all__ = ("celery_app",)

# CELERY_BROKER_URL = "redis://localhost:6379"
# CELERY_RESULT_BACKEND = "redis://localhost:6379"