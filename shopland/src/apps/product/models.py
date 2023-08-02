from django.db import models


# Созданы 2 модели Product и Category

class Category(models.Model):
    name = models.CharField("Название",max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Название", max_length=200)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена",max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to="products/images/")
    is_active = models.BooleanField("Активный", default=True)
    
    created = models.DateTimeField(verbose_name="Дата создание", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    class Meta:
        ordering = ["-created"] # Вывод товара по дате создания
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
    
    @property 
    def link(self):
        return f'https://127.0.0.1:8000/products/product/{self.id}' 
        # при помощи property создал атрибут из метода для получение ссылки на детальную страницу товара для Аминки