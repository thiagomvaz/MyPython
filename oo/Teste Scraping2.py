import requests
from bs4 import BeautifulSoup

busca = str(input('Digite o nome da imagem que deseja baixar: '))
quantidade_de_imagens = int(input('Quantas imagens deseja baixar: '))
#diretorio = str(input("Qual o diretório deseja salvar as imagens: "))
diretorio = '/home/thiago/Teste'

links_list = []
img_list = []
img_index = 0
page_number = (quantidade_de_imagens // 20) * 20

url1 = f'https://www.google.com/search?q={busca}&client=ubuntu&hs=XNB&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjK14ekku_8AhW8t5UCHb1xDN0Q_AUoAXoECAEQAw&biw=1206&bih=768&dpr=1'

req = requests.get(url1)
soup = BeautifulSoup(req.text, 'html.parser')

for img in soup.findAll('img')[1:]:
    if img_index == quantidade_de_imagens:
        break
    else:
        links_list.append(img.get('src'))
        img_index += 1

for links in links_list:
    img_list.append(requests.get(links))

for i, img in enumerate(img_list):
    with open(f'{diretorio}/{busca}_{i}.png', 'wb') as f: #wb = write byte
        f.write(img.content)