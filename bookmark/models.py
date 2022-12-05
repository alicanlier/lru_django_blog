from django.db import models
from django.contrib.auth.models import User

# Create your models here. DB tables을 만들어 주는 모델들 (VO classes)
class Bookmark(models.Model):
    #id 넘버링 필드는 자동으로 만들어준다
    title = models.CharField('TITLE',max_length=100,blank=True)
    url = models.URLField('URL',unique=True) #URL column's id
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    #java's toString
    #overriding str method #객체 표현 방식
    def __str__ (self):
        return self.title
    
