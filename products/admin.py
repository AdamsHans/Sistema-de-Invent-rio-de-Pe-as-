import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import EstoqueAtual, Entrada, Saida, ItemZerado, Emprestimo

# === Funções de exportação CSV ===

def exportar_estoque_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estoque_atual.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nº Cep', 'SP Number', 'Produto', 'Local', 'Quantidade'])
    for obj in queryset:
        writer.writerow([obj.numero_cep, obj.sp_number, obj.produto, obj.local, obj.quantidade])
    return response
exportar_estoque_csv.short_description = 'Exportar Estoque Atual para CSV'

def exportar_entrada_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="entradas.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nº Cep', 'SP Number', 'Produto', 'Local', 'Quantidade', 'Data', 'Observações'])
    for obj in queryset:
        writer.writerow([obj.numero_cep, obj.sp_number, obj.produto, obj.local, obj.quantidade, obj.data, obj.observacoes])
    return response
exportar_entrada_csv.short_description = 'Exportar Entradas para CSV'

def exportar_saida_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="saidas.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nº Cep', 'SP Number', 'Produto', 'Local', 'Quantidade', 'Data', 'Observações'])
    for obj in queryset:
        writer.writerow([obj.numero_cep, obj.sp_number, obj.produto, obj.local, obj.quantidade, obj.data, obj.observacoes])
    return response
exportar_saida_csv.short_description = 'Exportar Saídas para CSV'

def exportar_zerados_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="zerados.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nº Cep', 'SP Number', 'Produto', 'Local', 'Quantidade'])
    for obj in queryset:
        writer.writerow([obj.numero_cep, obj.sp_number, obj.produto, obj.local, obj.quantidade])
    return response
exportar_zerados_csv.short_description = 'Exportar Itens Zerados para CSV'

def exportar_emprestimos_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emprestimos.csv"'
    writer = csv.writer(response)
    writer.writerow(['Tipo', 'Nº Cep', 'SP Number', 'Produto', 'Quantidade', 'Data', 'Observações'])
    for obj in queryset:
        writer.writerow([obj.tipo, obj.numero_cep, obj.sp_number, obj.produto, obj.quantidade, obj.data, obj.observacoes])
    return response
exportar_emprestimos_csv.short_description = 'Exportar Empréstimos para CSV'

# === Admins ===

@admin.register(EstoqueAtual)
class EstoqueAtualAdmin(admin.ModelAdmin):
    list_display = ('numero_cep', 'sp_number', 'produto', 'local', 'quantidade')
    search_fields = ('sp_number', 'produto')
    list_filter = ('numero_cep', 'sp_number', 'produto', 'local', 'quantidade')
    actions = [exportar_estoque_csv]

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('numero_cep', 'sp_number', 'produto', 'local', 'quantidade', 'data')
    search_fields = ('sp_number', 'produto')
    list_filter = ('numero_cep', 'sp_number', 'produto', 'local', 'quantidade', 'data')
    actions = [exportar_entrada_csv]

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
    list_display = ('numero_cep', 'sp_number', 'produto', 'local', 'quantidade', 'data')
    search_fields = ('sp_number', 'produto')
    list_filter = ('numero_cep', 'sp_number', 'produto', 'local', 'quantidade', 'data')
    actions = [exportar_saida_csv]

@admin.register(ItemZerado)
class ItemZeradoAdmin(admin.ModelAdmin):
    list_display = ('numero_cep', 'sp_number', 'produto', 'local', 'quantidade')
    search_fields = ('numero_cep','sp_number', 'produto', 'local', 'quantidade')
    actions = [exportar_zerados_csv]

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'numero_cep', 'sp_number', 'produto', 'quantidade', 'data', 'observacoes')
    search_fields = ('sp_number', 'produto')
    list_filter = ('tipo', 'numero_cep', 'sp_number', 'produto', 'quantidade', 'data')
    actions = [exportar_emprestimos_csv]
