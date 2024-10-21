from django.db import models
class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name='Тэг')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, related_name='tags', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    # это будет отображаться при добавлении нового раздела в админке в центральной панели
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Сделать основным')

    # это заголовки форм
    class Meta:
        verbose_name = 'Тематика Статьи'
        verbose_name_plural = 'ТЕМАТИКИ СТАТЬИ'
