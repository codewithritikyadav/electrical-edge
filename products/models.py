from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    # Cover Image
    cover_image = models.ImageField(
    upload_to='books/covers/',
    null=True,
    blank=True
    )

    # Sample PDF
    sample_pdf = models.FileField(
        upload_to='books/samples/',
        storage=RawMediaCloudinaryStorage(),
        null=True,
        blank=True
    )

    # Full PDF
    full_pdf = models.FileField(
        upload_to='books/full/',
        storage=RawMediaCloudinaryStorage(),
        null=True,
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title