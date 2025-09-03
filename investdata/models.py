from django.db import models

class Stocks(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Nome',)
    price = models.FloatField(null=True, verbose_name='Preço',)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criando em',)

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'

    def __str__(self):
        return str(self.name)
