### 1. Создайте и активируйте virtual env
```sh
python -m venv venv 
```
##Windows
```sh
env\Scripts\activate
```

##Linux
```sh
source venv/bin/activate
```
### 2. Установка зависимостей
```sh
pip install -r requirements.txt
```
### 3. Создайте миграции
```sh
python manage.py makemigrations
```
### 4. Запустите миграции
```sh
python manage.py migrate
```
### 5. Запуск проекта
```sh
python manage.py runserver
```
#Запуск тестов
```sh
manage.py test
```
