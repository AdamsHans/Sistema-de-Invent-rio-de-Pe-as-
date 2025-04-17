import pandas as pd
import os
import sys
import django

# Caminho do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Configurações Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Inventario_CEP.settings')
django.setup()

from products.models import EstoqueAtual, Entrada, Saida, ItemZerado, Emprestimo

ARQUIVO = os.path.join(BASE_DIR, '11-23 Inventário de Peças-Novembro.xlsx')

def importar_estoque():
    df = pd.read_excel(ARQUIVO, sheet_name='Inventário')
    for _, row in df.iterrows():
        EstoqueAtual.objects.create(
            numero_cep=row['Nº Cep'],
            sp_number=row['SP Number'],
            local=row['Local'],
            quantidade=row['Quantidade'],
            produto=row['Produto']
        )
    print("✅ Estoque importado com sucesso.")

def importar_entrada():
    df = pd.read_excel(ARQUIVO, sheet_name='Entrada de Peças')
    for _, row in df.iterrows():
        Entrada.objects.create(
            numero_cep=row['Nº Cep'],
            sp_number=row['SP Number'],
            local=row['Local'],
            quantidade=row['Quantidade'],
            produto=row['Produto'],
            data=pd.to_datetime(row['Data']).date(),
            observacoes=row.get('Observações', '')
        )
    print("✅ Entradas importadas com sucesso.")

def importar_saida():
    df = pd.read_excel(ARQUIVO, sheet_name='Saída de Peças')
    for _, row in df.iterrows():
        Saida.objects.create(
            numero_cep=row['Nº Cep'],
            sp_number=row['SP Number'],
            local=row['Local'],
            quantidade=row['Quantidade'],
            produto=row['Produto'],
            data=pd.to_datetime(row['Data']).date(),
            observacoes=row.get('Observações', '')
        )
    print("✅ Saídas importadas com sucesso.")

def importar_zerados():
    df = pd.read_excel(ARQUIVO, sheet_name='Peças Estoque 0')
    for _, row in df.iterrows():
        ItemZerado.objects.create(
            numero_cep=row['Nº Cep'],
            sp_number=row['SP Number'],
            local=row['Local'],
            quantidade=row['Quantidade'],
            produto=row['Produto']
        )
    print("✅ Itens zerados importados com sucesso.")

def importar_emprestimos(tipo, skip_rows, nrows):
    df = pd.read_excel(ARQUIVO, sheet_name='Empréstimos', skiprows=skip_rows, nrows=nrows)
    for _, row in df.iterrows():
        data = row.get('Data')
        if pd.isnull(data):
            data = '2023-11-01'
        data = pd.to_datetime(data).date()

        Emprestimo.objects.create(
            tipo=tipo,
            numero_cep=row['Nº Cep'],
            sp_number=row['SP Number'],
            quantidade=row['Quantidade'],
            produto=row['Produto'],
            data=data,
            observacoes=row.get('Observações', '')
        )
    print(f"✅ Empréstimos ({tipo}) importados com sucesso.")

if __name__ == '__main__':
    importar_estoque()
    importar_entrada()
    importar_saida()
    importar_zerados()

    importar_emprestimos('nossas', skip_rows=2, nrows=5)
    importar_emprestimos('conserto', skip_rows=10, nrows=5)
    importar_emprestimos('terceiros', skip_rows=18, nrows=5)
