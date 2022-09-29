from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

# Adicionando, deletando, etc nosso script
#repo.insert('Algum_filme_Eddy2', 'ação', 2022)
repo.delete('Duna')

data = repo.select()
print(data)



import pandas as pd
df = pd.DataFrame(data)
print(df.head(20))




