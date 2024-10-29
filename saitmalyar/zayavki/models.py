from django.db import models
from django.utils import timezone


class Articles(models.Model):
    name = models.CharField("Имя/Фамилия", max_length=50)
    phone = models.IntegerField("Номер телефона", max_length=15)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"