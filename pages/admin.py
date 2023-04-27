from django.contrib import admin
from .models import Category, Brand, Product, ProductImage


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "quantity", "slug", "is_available", "category", "category")
    list_display_links = ("pk", "title")
    list_filter = ("brand", "category")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProductImageInline]
    list_editable = ("is_available",)
