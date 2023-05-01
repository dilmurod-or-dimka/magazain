from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def get_absolute_url(self):
        return reverse("category_products", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    title = models.CharField(verbose_name="Название бренда", max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Product(models.Model):
    title = models.CharField(verbose_name="Название товара", max_length=150, unique=True)
    descr = models.TextField(verbose_name="Описание товара")
    price = models.IntegerField(verbose_name="Стоимость товара")
    quantity = models.IntegerField(verbose_name="Количество товара")
    is_available = models.BooleanField(verbose_name="Есть в наличии?", default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def get_first_photo(self):
        photo = self.productimage_set.all().first()
        if photo is not None:
            return photo.photo.url
        return "https://cs8.pikabu.ru/post_img/big/2016/09/10/4/1473482891145853538.jpg"

    def get_second_photo(self):
        try:
            photo = self.productimage_set.all()[1]
            if photo is not None:
                return photo.photo.url
        except Exception as e:
            return "data:image/png;base64,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"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="products/", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
