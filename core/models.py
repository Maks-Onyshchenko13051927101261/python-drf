from django.db import models


# Базова модель зі спільними полями для інших моделей
class CoreConfig(models.Model):
    # Вказуємо, що модель абстрактна і не створює власної таблиці в БД
    class Meta:
        abstract = True

    # Автоматично записує дату й час створення об'єкта
    created_at = models.DateTimeField(auto_now_add=True)

    # Автоматично оновлює дату й час під час збереження об'єкта
    updated_at = models.DateTimeField(auto_now=True)
