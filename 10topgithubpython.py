

#Jennifer Nicholas
#Published on 01-Apr-2019 16:22:13
#Fetch top 10 starred repositories of user on GitHub using Python?
#https://www.tutorialspoint.com/fetch-top-10-starred-repositories-of-user-on-github-using-python

import requests
from bs4 import BeautifulSoup
r = requests.get('https://github.com/trending/lua?since=monthly')
bs = BeautifulSoup(r.text, 'lxml')
lista_repo = bs.find_all('ol', class_='repo-list')
f1 = open('starred-repos.txt', 'w')
for lr in lista_repo:
   aux = lr.find_all('div', class_='d-inline-block col-9 mb-1')
   for ld in aux:
      rank = ld.find_all('a')
      f1.writelines(str(rank))
      f1.writelines('\n')
f1.close()
f1 = open('starred-repos.txt', 'r')
texto = []
for x in f1:
   if x[0] == '[' and x[1] == '<' and x[2] == 'a':
      na = x.split('"')
      texto.append(na[1])
f1.close()
f1 = open('starred-repos.txt', 'w')
f1.writelines('{}\t {}\t\t {}\t\n\n'.format('Position ', 'Name ', 'Repositories '))
for i in range(10):
   tex= texto[i].split('/')
   name = tex[1]
   repos = tex[2]
   f1.writelines('{}- \t {}\t\t {}'.format(i + 1, name, repos))
   f1.writelines('\n')
f1.close()
f1 = open('starred-repos.txt', 'r')
print(f1.read())
f1.close()