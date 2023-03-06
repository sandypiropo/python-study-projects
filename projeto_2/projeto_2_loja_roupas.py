
"""Projeto para estudo n°2 criado no Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b8jLZrTaF7C8WTypN7ISN0NIXS75OMBi
"""

import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_excel("/content/Vendas.xlsx")
display(tabela)

faturamento_total = tabela['Valor Final'].sum()
print(faturamento_total)

faturamento_por_lojas = tabela[['Valor Final', 'Produto', 'ID Loja']].groupby(
    ["ID Loja", "Produto"]).sum().sort_values(by='Valor Final', ascending=False)
print(faturamento_por_lojas)

# Criando o primeiro dataframe com os dados
faturamento_por_lojas = tabela[['Valor Final', 'Produto', 'ID Loja']].groupby(
    ["ID Loja", "Produto"]).sum()
faturamento_por_lojas = faturamento_por_lojas.unstack()
faturamento_por_lojas.columns = faturamento_por_lojas.columns.droplevel()
faturamento_por_lojas = faturamento_por_lojas.sort_values(
    by='Bermuda Liso', ascending=False)
faturamento_por_lojas.plot(kind='bar', figsize=(15, 9))
plt.xlabel('Loja')
plt.ylabel('Faturamento')
plt.title('Faturamento por loja e produto')
plt.show()

# Agrupando vendas por loja para segundo dataframe
vendas_por_loja = tabela.groupby("ID Loja")["Valor Final"].sum()
# Criando o  eixo
fig, ax = plt.subplots(figsize=(15, 9))
# Criando o gráfico de barras
ax.bar(vendas_por_loja.index, vendas_por_loja.values)
# Configurando os labels do gráfico
ax.set_title("Vendas Totais por Loja")
ax.set_xlabel("ID Loja")
ax.set_ylabel("Valor Total (R$)")
# Exibindo o gráfico
plt.show()


"""Os modelos de Bermuda que mais se destacam são o Bermuda Liso, que foi vendido em maior quantidade no Iguatemi Campinas, e o Bermuda Listrado, que teve um bom desempenho no Bourbon Shopping SP e no Norte Shopping. Já o modelo que teve o menor desempenho foi o Bermuda, que foi vendido em menor quantidade no Norte Shopping e no Iguatemi Campinas.

Também foi possível observar que alguns shoppings têm uma preferência por determinados modelos de Bermuda, como é o caso do Center Shopping Uberlândia, que teve um bom desempenho nas vendas de Bermudas de linho e estampadas.
"""
