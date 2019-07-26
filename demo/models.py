from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from db.base_model import BaseModel


# Create your models here.

class Goods(BaseModel):
    """
    商品
    """
    name = models.CharField(default="", max_length=30, verbose_name="商品名称", help_text="商品名称")
    content = RichTextUploadingField(blank=True, verbose_name='内容描述')

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
