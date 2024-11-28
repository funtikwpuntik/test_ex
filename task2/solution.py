import requests
from bs4 import BeautifulSoup
import csv

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
animals = {}

groups = soup.find_all('div', class_='mw-category-group')
links = soup.find('div', id='mw-pages').find_all('a', title='Категория:Животные по алфавиту')
count = 0
while True:
    for group in groups:
        for i in group.find_next('ul').find_all('li'):
            animal = i.text
            if animal[0] == ' ':
                continue
            animals[animal[0]] = animals.get(animal[0], 0) + 1
    links = soup.find('div', id='mw-pages').find_all('a', title='Категория:Животные по алфавиту')
    if links[-1].text == 'Предыдущая страница':
        break
    url = 'https://ru.wikipedia.org' + links[-1]['href']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    groups = soup.find_all('div', class_='mw-category-group')
    count += 1
    print(f'Страница {count} обработана')


data = [[key,value] for key, value in animals.items()]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)