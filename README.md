# Проект "Мое домашнее задание по уроку 10.1"

## Описание:
В данном домашнем задании мы познакомились с [GitHub](https://github.com) — сервисом, в котором хранят свои проекты разработчики. Привязали наш аккаунт GitHub к локальному репозиторию и настроили доступ через токен или SSH-ключ.
Изучили концепцию GitFlow — модели ветвления, которая помогает эффективно работать с Git в команде. Рассмотрели основные типы веток, которые используются в GitFlow.
Погрузились в работу с ветками. Ветки — это мощный инструмент, который позволяет работать над разными функциями и исправлениями в коде параллельно. Научились создавать, переключаться и удалять их.
Научились делать слияние веток, чтобы объединить несколько исправлений в одну единую историю изменений. Узнали, в чём разница между способами слияния 
merge и rebase. Научились выполнять слияние веток в своем проекте, выбирая подходящий метод в зависимости от задачи.

В домашнем задании этого урока мы продолжили работать над проектом. Отправили свой локальный Git-репозиторий на GitHub. Начали работать по GitFlow, разделяя код на ветки, 
и расширите приложение дополнительными функциями работы с данными о банковских операциях пользователя. Научились создавать READMY.md для описания проекта.

## Инструкции по установке проекта:
- **Создаем аккаунт на GitHub**:
- **Привязываем GitHub-аккаунт по персональному токену или SSH-ключу**
- **Создаем репозиторий на GitHub и связываем с локальным**
- **Создаем Pull request**

Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```

Домашнее задание сдайем на проверку наставнику ссылкой на пул-реквест.
Посмотрите инструкцию, как сдавать домашку с помощью [пул-реквеста](https://my.sky.pro/student-cabinet/stream-lesson/131743/homework-requirements).

## Информация о зависимостях:

2. Установите зависимости:
```
pip install -r requirements.txt
```
```
[tool.poetry]
name = "pythonproject1"
version = "0.1.0"
description = ""
authors = ["Stanislav Danilov <ScaM79@mail.ru>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.12"
requests = "^2.32.3"


[tool.poetry.group.lint.dependencies]
flake8 = "^7.1.0"
mypy = "^1.10.1"
black = "^24.4.2"
isort = "^5.13.2"
```

## Шаги конфигурации (Настройки)

```
[tool.mypy]
disallow_untyped_defs = true
no_implicit_optional = true
warn_return_any = true
exclude = 'venv'

[tool.black]
# Максимальная длина строки
line-length = 119
# Файлы, которые не нужно форматировать
exclude = '''
(
  /(
      \.eggs         # Исключить несколько общих каталогов
    | \.git          # в корне проекта
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | dist
  )/
  | foo.py           # Также отдельно исключить файл с именем foo.py
                     # в корне проекта
)
'''

[tool.isort]
# максимальная длина строки
line_length = 119

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
## Тесты:
В папку tests добавлены тесты:
[test_masks.py](tests%2Ftest_masks.py)

[test_processing.py](tests%2Ftest_processing.py)

[test_widget.py](tests%2Ftest_widget.py)

для тестирования функций, а так же файл [conftest.py](tests%2Fconftest.py)
который содержит фикстуры.

### Покрытие тестами:

File	function	                     statements	   missing	  excluded	coverage

src\__init__.py	(no function)	            0	          0	          0	      100%

src\masks.py	get_mask_card_number	      3	          0	          0	      100%

src\masks.py	get_mask_account	          3	          0	          0	      100%

src\masks.py	(no function)	              2	          0	          0	      100%

src\processing.py	filter_by_state	        5	          0	          0	      100%

src\processing.py	sort_by_date	          1	          0	          0	      100%

src\processing.py	(no function)	          2	          0	          0	      100%

src\widget.py	mask_account_cart	         24	          5	          0	      79%

src\widget.py	get_data	                  6	          0	          0	      100%

src\widget.py	(no function)	              7	          2	          0	      71%

**Total	 	                               53	          7	          0	      87%**

coverage.py v7.6.0, created at 2024-07-31 00:09 +0700

## Документация:
Дополнительную информацию о условиях и способах сдачи можно посмотреть на сайте [https://my.sky.pro](https://my.sky.pro/student-cabinet/stream-lesson/131743/homework-requirements).

## Лицензия:
Проект распространяется под [лицензией MIT](LICENSE).
