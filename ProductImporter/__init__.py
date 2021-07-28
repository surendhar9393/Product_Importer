
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import celery_app

__all__ = ['celery_app']

__version__ = '2017.1.0'
__version_info__ = tuple([int(num) if num.isdigit() else
    num for num in __version__.replace('-', '.', 1).split('.')])

