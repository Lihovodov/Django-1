from django.db import models

class Article(models.Model):
	article_title =models.CharField('название статьи',max_length=200)
	article_text = models.TextField('текст статьи')
	
	class Meta:
		verbose_name='Статья'
		verbose_name_plural='Статьи'


	def __str__(self):
		return self.article_title


class Comment(models.Model):
	article =models.ForeignKey(Article,on_delete =models.CASCADE)
	name_author =models.CharField('имя автора',max_length=50)
	comment_text =models.CharField('текст коментария',max_length=250)
	class Meta:
		verbose_name='коментарий'
		verbose_name_plural='коментарии'