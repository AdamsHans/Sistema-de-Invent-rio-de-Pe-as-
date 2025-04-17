from django.db import models


class EstoqueAtual(models.Model):
    numero_cep = models.CharField(max_length=20, verbose_name='Nº Cep')
    sp_number = models.CharField(max_length=50, verbose_name='SP Number')
    local = models.CharField(max_length=100, verbose_name='Local')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    produto = models.CharField(max_length=200, verbose_name='Produto')

    class Meta:
        verbose_name = 'Estoque Atual'
        verbose_name_plural = 'Estoque Atual'
        ordering = ['produto']

    def __str__(self):
        return f"{self.sp_number} - {self.produto}"


class Entrada(models.Model):
    numero_cep = models.CharField(max_length=20, verbose_name='Nº Cep')
    sp_number = models.CharField(max_length=50, verbose_name='SP Number')
    local = models.CharField(max_length=100, verbose_name='Local')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    produto = models.CharField(max_length=200, verbose_name='Produto')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')

    class Meta:
        verbose_name = 'Entrada de Peça'
        verbose_name_plural = 'Entradas de Peças'
        ordering = ['-data']

    def __str__(self):
        return f"Entrada: {self.produto} ({self.quantidade})"


class Saida(models.Model):
    numero_cep = models.CharField(max_length=20, verbose_name='Nº Cep')
    sp_number = models.CharField(max_length=50, verbose_name='SP Number')
    local = models.CharField(max_length=100, verbose_name='Local')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    produto = models.CharField(max_length=200, verbose_name='Produto')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')

    class Meta:
        verbose_name = 'Saída de Peça'
        verbose_name_plural = 'Saídas de Peças'
        ordering = ['-data']

    def __str__(self):
        return f"Saída: {self.produto} ({self.quantidade})"


class ItemZerado(models.Model):
    numero_cep = models.CharField(max_length=20, verbose_name='Nº Cep')
    sp_number = models.CharField(max_length=50, verbose_name='SP Number')
    local = models.CharField(max_length=100, verbose_name='Local')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    produto = models.CharField(max_length=200, verbose_name='Produto')

    class Meta:
        verbose_name = 'Peça com Estoque Zerado'
        verbose_name_plural = 'Peças com Estoque Zerado'
        ordering = ['produto']

    def __str__(self):
        return f"{self.produto} (Zerado)"


class Emprestimo(models.Model):
    TIPO_EMPRESTIMO = [
        ('nossas', 'Peças nossas em poder de terceiros'),
        ('conserto', 'Envio de peças para conserto'),
        ('terceiros', 'Peças de terceiros em nosso poder'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_EMPRESTIMO, verbose_name='Tipo de Empréstimo')
    numero_cep = models.CharField(max_length=20, verbose_name='Nº Cep')
    sp_number = models.CharField(max_length=50, verbose_name='SP Number')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    produto = models.CharField(max_length=200, verbose_name='Produto')
    data = models.DateField(verbose_name='Data')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['tipo', 'produto']

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.produto}"