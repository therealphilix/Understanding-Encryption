from typing import Iterable
from django.db import models
from .encryption import encrypt_data, decrypt_data

# Create your models here.
class Profile(models.Model):
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    encrypted_phone = models.CharField(max_length=15, blank=True)
    encrypted_address = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.encrypted_phone = encrypt_data(self.phone)
        self.encrypted_address = encrypt_data(self.address)
        return super().save(*args, **kwargs)
    
    def get_decrypted_data(self):
        return {
            'phone': decrypt_data(self.encrypted_phone),
            'address': decrypt_data(self.encrypted_address)
        }