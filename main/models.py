from django.db import models

class TableBase(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ученики'
        verbose_name_plural = 'Ученики'

        
