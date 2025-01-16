from django.db import models
from django.utils.translation import gettext_lazy as _


class Image(models.Model):
    file = models.ImageField(
        upload_to="images/", verbose_name=_("File"), help_text=_("The image file")
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Description"),
        help_text=_("Optional description of the image"),
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Uploaded At"),
        help_text=_("The date and time when the image was uploaded"),
    )

    class Meta:
        abstract = True  # Oznacza, że nie będzie tabeli w bazie dla tego modelu
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return self.file.name if self.file else "No File"
