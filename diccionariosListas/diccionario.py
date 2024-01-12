#!/usr/bin/env python3

peliculas = dict()

peliculas['Star Wars'] = 'George Lucas'
peliculas['Terminator'] = 'James Cameron'
peliculas['Blade Runner'] = 'Ridley Scott'
peliculas['Lord of the Rings'] = 'Peter Jackson'
peliculas['Robocop'] = 'Paul Verhoeven'

print(len(peliculas), 'peliculas en nuestra coleccion')
if 'Star Wars' in peliculas:
    print('Tenemos Star Wars')

print('Las peliculas son:')
for peli in list(peliculas.keys()):
    print('-', peli)

# Un diccionario es iterable, tambien lo podemos recorrer asi:
print('Las peliculas son:')
for key in peliculas:
    print('-', key)
    