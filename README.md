# Пульт охраны - это сайт, который можно подключить к удаленной базе данных с визитами и карточками пропуска сотрудников.

## Установка
Клонируем репозиторий:
```
git clone https://github.com/malykhdenis/dvmn_django-orm-watching-storage/
```

Переходим в папку с проектом:
```
cd dvmn_django-orm-watching-storage
```

Устанавливаем и активируем venv:
```
python3 -m venv venv
```

```
source venv/bin/activate
```

Устанавливаем pip:
```
python3 -m pip install --upgrade pip
```

Устанавливаем зависимости:
```
pip install -r requirements.txt
```

Запускаем проект:
```
python3 manage.py runserver
```

Проект будет доступен по адресу:
```http://127.0.0.1:8000/```
