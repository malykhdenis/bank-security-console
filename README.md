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

## stop_virus.py

Среди сотрудников компании стремительно распространяется опасный вируc. Один за другим они уходят на больничный. Эпидемия нарастает, пора принимать решительные действия. Найдите всех сотрудников, контактировавших с заболевшими.

Скрипт принимает два аргумента — имя заболевшего и дату заболевания. В консоль скрипт выведет имена тех, кто оказался в группе риска. Рискуют здоровьем те, кто в течение недели до болезни оказался в хранилище одновременно с заболевшим.

Пример ввода в консоль:
```
python stop_virus.py --patient 'Neymar Junior' --date 2023-12-12
```
Список контактных сотрудников будет выведен в виде таблицы с указанием имени сотрудника и даты контакта.
