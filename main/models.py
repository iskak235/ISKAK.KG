from django.db import models


class MyHistory(models.Model):
    CATEGORY_CHOICES = [
        ('STUDY', 'Окуган жерим'),
        ('VILLAGE', 'Айылым'),
        ('FRIENDS', 'Досторум'),
        ('WORK', 'Иштеген жерим'),
        ('GAMES', 'Оюндарым'),
    ]

    title = models.CharField(max_length=200, verbose_name="Темасы")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Бөлүм")
    description = models.TextField(verbose_name="Маалымат")
    image = models.ImageField(upload_to='photos/', verbose_name="Сүрөт")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"