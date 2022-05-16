# Django Import:
from django.db.models import Manager


# Managers class:
class BasicManager(Manager):

    def get_queryset(self):
        return super(
            BasicManager, self
        ).get_queryset().filter(deleted=False)


class ActiveManager(Manager):

    def get_queryset(self):
        return super(
            ActiveManager, self
        ).get_queryset().filter(deleted=False, status=1)
