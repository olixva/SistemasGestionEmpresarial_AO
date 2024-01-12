
peliculas = dict()
peliculas['Star Wars'] = 'George Lucas'
peliculas['Terminator'] = 'Pedro Almodovar'

# Modificamos una de las entradas
peliculas['Terminator'] = 'James Cameron'

# Anadimos dos entradas nuevas 
peliculas['Lord of the Rings'] = 'Peter Jackson'
peliculas['Alien'] = 'Ridley Scott'

# Eliminamos entradas del diccionario, dos formas:
del peliculas['Star Wars']
peliculas.pop('Lord of the Rings')

print('Las peliculas de nuestra coleccion son:')
for key in peliculas:
    print('- {0} ({1})'.format(key, peliculas[key]))
