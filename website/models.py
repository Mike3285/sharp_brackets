from django.db import models

# Create your models here.


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    email = models.EmailField(max_length=100, default="")
    oggetto = models.CharField(max_length=100, default="")
    testo = models.TextField(default="")
    has_accepted = models.BooleanField(default=False)
    ip_address = models.CharField(max_length=100, default="")
    class Meta:
        verbose_name = "Messaggio"
        verbose_name_plural = "Messaggi"