from django.db import models

class TelephoneBlock(models.Model):
    title = models.CharField(max_length=100, default="", blank=True, null=True)

    def __str__(self):
        return self.title

class TelephoneUnit(models.Model):
    title = models.CharField(max_length = 100, default="", blank=True, null=True)
    description = models.TextField(default="", blank=True, null=True)
    telephoneUnit = models.ForeignKey(TelephoneBlock, related_name="telephoneUnit", on_delete=models.CASCADE, blank=True, null=True)
