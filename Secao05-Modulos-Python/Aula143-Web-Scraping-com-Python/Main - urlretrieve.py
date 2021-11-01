import urllib.request

print('Baixando capa do seu curso...')

url = 'https://i.udemycdn.com/course/240x135/2411816_3802_3.jpg'
urllib.request.urlretrieve(url, './seu_curso.jpg')

print('Capa do seu curso baixado com sucesso!')

