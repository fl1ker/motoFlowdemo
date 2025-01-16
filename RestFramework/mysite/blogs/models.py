from django.db import models
from django.utils.translation import gettext_lazy as _
from media.models import Image


class BlogContent(models.Model):
    title = models.CharField(
        max_length=200, verbose_name=_("Title"), help_text=_("Title of the blog post")
    )
    content = models.TextField(
        verbose_name=_("Content"), help_text=_("Main content of the blog post")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created At"),
        help_text=_("The date and time when the blog post was created"),
    )
    author_name = models.CharField(
        max_length=100,
        verbose_name=_("Author Name"),
        help_text=_("Name of the author of the blog post"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Blog Content")
        verbose_name_plural = _("Blog Contents")
        ordering = ["-created_at"]


class Blog(models.Model):
    blog_content = models.OneToOneField(
        BlogContent,
        on_delete=models.CASCADE,
        related_name="blog",
        verbose_name=_("Blog Content"),
        help_text=_("Detailed content of the blog"),
    )
    comments = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Comments"),
        help_text=_("Comments related to the blog post"),
    )

    def __str__(self):
        return f"Blog: {self.blog_content.title}"

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")


class BlogImage(Image):
    blog_content = models.ForeignKey(
        BlogContent,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name=_("Blog Content"),
        help_text=_("The blog post this image belongs to"),
    )
