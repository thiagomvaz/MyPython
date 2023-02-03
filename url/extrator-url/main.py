#url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = ' '

# Sanitização da URL
# url = url.replace(" ", "")
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_base)
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)


