# Django Import:
from django.db.models import Manager


# Managers class:
class BasicManager(Manager):

    def get_queryset(self):
        return super(
            BasicManager, self
        ).get_queryset().filter(deleted=False)


class ChangeLogManager(Manager):

    def get_queryset(self):
        return super(
            ChangeLogManager, self
        ).get_queryset().filter(deleted=False, active=True)
