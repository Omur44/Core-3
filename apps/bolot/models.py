from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Называие компании")
    address = models.CharField(max_length=100, verbose_name="Адрес компании")
    phone = models.CharField(max_length=100, verbose_name="Телефон компании")
    email = models.CharField(max_length=100, verbose_name="Email компании")
    description = models.TextField(verbose_name="Описание компании")
    logo = models.ImageField(upload_to='logo/', verbose_name="Логотип компании")
    working_hours = models.CharField(max_length=100, verbose_name="Время работы компании")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компании"

# Create your models here.
