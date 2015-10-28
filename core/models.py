from django.db import models


class EmailSubscribe(models.Model):
    email = models.EmailField(unique=True)
    signup_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
