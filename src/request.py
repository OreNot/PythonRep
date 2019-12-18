import requests

r = requests.get('https://vkusomania.av.ru/main');
print(r.text);
print(r.cookies);