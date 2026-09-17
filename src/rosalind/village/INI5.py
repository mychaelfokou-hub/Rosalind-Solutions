# Legge tutte le righe del file in una lista
with open('input_init5.txt', 'r') as file:
    lines = file.readlines()

# Le righe sono in un array, e le estraggo seondo la sintassi [posizione d'inizio : fine : passo]
even_lines = lines[1::2]

for x in even_lines:
    print(x.strip())