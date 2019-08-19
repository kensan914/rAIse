from django.db import models
from django.contrib.auth.models import User


class Pattern(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザ', on_delete=models.CASCADE)
    pattern_text = models.CharField(verbose_name='パターン', max_length=100, blank=True)
    output_text = models.TextField(verbose_name='返答', blank=True)
