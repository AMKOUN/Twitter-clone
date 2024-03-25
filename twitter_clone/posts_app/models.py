from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    text = models.TextField(
        verbose_name="текст",
        help_text = 'текст поста'
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Отображает дату публикации записи'
    )

    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,#теперь при удалении юзера из бд будут удалены все его посты
        related_name='posts',#нужно для будущей связи полей
        verbose_name='Автор',
        help_text='Отображает имя автора'
    )

    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='Ваша группа',
        verbose_name='Группа',
    )

    def __str__(self):
        return self.text

class Group(models.Model):
    title = models.CharField(
        max_length = 200,
        verbose_name='Название(заголовок)',
        help_text='Отображает название',
    )

    slug = models.SlugField(
        verbose_name='Уникальный адрес',
        help_text='Присвоение уникального адреса',
    )

    description = models.TextField(
        verbose_name='Описание',
        help_text='Отображает описание группы'
    )

    class Meta:
        ordering = ('-pub_date',),

    def __str__(self):
        return self.title