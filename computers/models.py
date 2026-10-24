from django.db import models


class Computer(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    ram_gb = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model}"
