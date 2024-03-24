from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """the learning topic of user"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)#自动获取当前时间
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.text
    
"""Topic 继承自 Model即django中定义了模型基本功能的类。我们给Topic类添加了两类
属性：text和date_added。
text属性存储少量文本可使用CharField"""

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)

    text = models.TextField()
    dete_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:

       verbose_name_plural = 'entries'
        
    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text