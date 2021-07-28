from django.db import models

# Create your models here.
from django.db import models
 
# Create your models here.
class QuestionModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    answer1 = models.CharField(max_length=200,null=True)
    answer2 = models.CharField(max_length=200,null=True)
    answer2 = models.CharField(max_length=200,null=True)
    answer2 = models.CharField(max_length=200,null=True)
    answer2 = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question