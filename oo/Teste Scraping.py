# Para extrair imagens do Google Imagens usando Python, Selenium e WebDriver, você pode
# seguir os seguintes passos:

# 1 - Instale as dependências:
#pip install selenium

#2 - Faça o download do WebDriver do navegador que deseja usar.Por exemplo, se
#você quiser usar o Chrome, pode baixar o ChromeDriver em
#https: // chromedriver.chromium.org /.

#3 - Abra o WebDriver e inicie uma sessão do navegador:
from selenium import webdriver

# Inicie uma sessão do Chrome
driver = webdriver.Chrome('/home/thiago/Downloads/chromedriver')

# Abra o Google Imagens
driver.get('https://www.google.com/imghp')

# 4 - Faça uma pesquisa de imagem usando o campo de pesquisa do Google Imagens:
# Encontre o campo de pesquisa
search_box = driver.find_element("name", "q")

# Digite a sua pesquisa
search_box.send_keys('gatos')

# Envie o formulário
search_box.submit()

# 5 - Encontre as imagens da pesquisa:
# Encontre todas as imagens da pesquisa
images = driver.find_element("css selector", ".rg_i")


# Imprima o número de imagens encontradas
#print(f'Encontrei {len(images)} imagens')

# 6 - Faça o download das imagens:
import requests

# Para cada imagem encontrada
for image in images:
    # Extraia o URL da imagem
    image_url = image.get_attribute('src')

    # Faça o download da imagem
    response = requests.get(image_url)

    # Salve a imagem em disco
    open(f'image_{i}.jpg', 'wb').write(response.content)

    # Incremente o contador
    i += 1


