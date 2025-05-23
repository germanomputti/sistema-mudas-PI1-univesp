"""
Script para inserir espécies de plantas no banco de dados.

Uso recomendado:
  python manage.py shell < catalogo/scripts/inserir_especies.py

Este script deve ser executado manualmente.
Antes de rodar o script, precisa ativar o ambiente virtual:
source venv/bin/activate

e também exportar a variavel de ambiente, que nesse caso é:
export DATABASE_URL='postgresql://mudas_db_user:4YPv32uGKz2rF1Ij3a00HzAyhqcONzvh@dpg-d0nma8idbo4c73c8v7g0-a.oregon-postgres.render.com:5432/mudas_db'
"""


from catalogo.models import Especie

dados = [
    ("Rosa", 75, 135, 5.00, 12.00),
    ("Girassol", 25, 80, 2.50, 8.00),
    ("Orquídea", 270, 900, 25.00, 80.00),
    ("Antúrio", 150, 450, 10.00, 30.00),
    ("Lírio", 50, 105, 4.00, 14.00),
    ("Gérbera", 50, 105, 3.00, 8.00),
    ("Cravo", 40, 100, 2.50, 6.00),
    ("Astromélia", 75, 135, 4.00, 14.00),
    ("Margarida", 40, 105, 2.00, 6.00),
    ("Lavanda", 75, 165, 3.50, 12.00),
    ("Zínnia", 25, 70, 2.00, 5.00),
    ("Camomila", 25, 75, 2.00, 5.00),
]

for nome, muda, flor, preco_muda, preco_flor in dados:
    Especie.objects.create(
        nome=nome,
        dias_ate_muda=muda,
        dias_ate_flor=flor,
        preco_muda=preco_muda,
        preco_flor=preco_flor
    )