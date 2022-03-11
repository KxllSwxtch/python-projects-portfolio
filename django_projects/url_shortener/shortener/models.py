from django.db import models


class Url(models.Model):
    """
    A simple URL model
    """
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)

    def __str__(self):
        return self.uuid
