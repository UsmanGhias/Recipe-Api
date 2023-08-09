from django.core.management.base import BaseCommand

"""
_summary_
Django command to pause execution until database is available
"""


class Command(BaseCommand):
    """
    _summary_
    Django Command to wait for database
    """

    def handle(self, *args, **options):

        pass
