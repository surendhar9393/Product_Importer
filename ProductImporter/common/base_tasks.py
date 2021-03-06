from celery.app.task import Task
from django.db import transaction


class TransactionAwareTask(Task):
    '''
    Task class which is aware of django db transactions and only executes tasks
    after transaction has been committed
    '''
    abstract = True

    def apply_async(self, *args, **kwargs):
        '''
        Unlike the default task in celery, this task does not return an async
        result
        '''
        transaction.on_commit(
            lambda: super(TransactionAwareTask, self).apply_async(
                *args, **kwargs))
