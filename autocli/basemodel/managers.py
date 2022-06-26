# Django Import:
from django.db.models import Manager

# Import change model:
from changes.models.change_model import Change


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
        ).get_queryset().filter(deleted=False)
