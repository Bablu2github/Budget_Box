from django.db import models

class User(models.Model):
    class Meta(object):
        db_table = 'user'

    email = models.CharField(
        'Email', blank=False, null=False, max_length=50
    )
    password = models.CharField(
        'Password', blank=False, null=False, max_length=50
    )
    token = models.CharField(
        'Token', blank=True, null=True, max_length=500, db_index=True
    )
    token_expires = models.DateTimeField(
        'Token Expiration Date', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Creation Date', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Update Date', blank=True, auto_now=True
    )

    def __str__(self):
        return self.email