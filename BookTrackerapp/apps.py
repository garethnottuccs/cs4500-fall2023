"""
This is the apps module for the BookTrackerapp application
"""

from django.apps import AppConfig


class BookTrackerappConfig(AppConfig):
    """
    This is the configuration class for the BookTrackerapp application
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BookTrackerapp'
