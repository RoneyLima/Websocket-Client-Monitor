from model.Core_Conta_Soldas import conta_soldas, engine

conn = engine.connect()

ins = conta_soldas.insert()

conn.execute(conta_soldas.insert(), [
    {'eletrodo': 1, 'soldagens':0},
    {'eletrodo': 2, 'soldagens':0},
    {'eletrodo': 3, 'soldagens':0},
    {'eletrodo': 4, 'soldagens':0},
    {'eletrodo': 5, 'soldagens':0},
    {'eletrodo': 6, 'soldagens':0},
    {'eletrodo': 7, 'soldagens':0},
    {'eletrodo': 8, 'soldagens':0},
    {'eletrodo': 9, 'soldagens':0},
    {'eletrodo': 10, 'soldagens':0},
    {'eletrodo': 11, 'soldagens':0},
    {'eletrodo': 12, 'soldagens':0},
    {'eletrodo': 13, 'soldagens':0},
    {'eletrodo': 14, 'soldagens':0},
    {'eletrodo': 15, 'soldagens':0}
])

