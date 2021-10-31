#Exercicio 1
df_mes = df[['vacina_dataaplicacao']]
df_mes['vacina_mesaplicacao'] = df_mes['vacina_dataaplicacao'].str.slice(0,7)
print(df_mes['vacina_mesaplicacao'].value_counts())

#Exercicio 2
df[df['vacina_dataaplicacao'] == '2021-10-17']
