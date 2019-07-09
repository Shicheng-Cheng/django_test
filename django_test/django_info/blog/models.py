from django.db import models

# Create your models here.
class Article(models.Model):
    article_id=models.AutoField(primary_key=True)
    title=models.TextField()
    brief_content=models.TextField()
    content=models.TextField()
    publish_data=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


#创建应用的数据库表结构，其中id是自增主键，题目，主要内容，内容都是文本类型，还有发布日期为时间类型。