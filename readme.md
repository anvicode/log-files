# Консольное приложение для работы с лог-файлами

## Описание задачи:

Создать консольное приложение на Python, которое будет анализировать лог-файлы. Предположим, что каждая строка лог-файла имеет следующий формат: дата и время события, уровень важности (INFO, WARNING, ERROR), и сообщение об ошибке или событии.

## Приложение должно поддерживать следующие функции:

- [x] Чтение лог-файла: Приложение должно прочитать лог-файл и отобразить его содержимое.
  - [x] Чтение лог-файла целиком
- [x] Фильтрация по уровню важности: Пользователь может указать уровень важности (INFO, WARNING, ERROR), и приложение должно отобразить только записи с этим уровнем важности.
- [x] Поиск по ключевым словам: Пользователь может ввести ключевое слово, и приложение должно отобразить все записи, содержащие это слово.
- [x] Сортировка записей: Пользователь может выбрать, сортировать ли записи по дате и времени в прямом или обратном порядке.

- [x] Сохранение состояния списка с логами
- [x] Ресет фильтров
- [x] Удобный вывод в консоль

## Основные требования:

- [x] Реализовать функционал с использованием встроенных функций Python для работы с файлами.
- [x] Обработать возможные исключительные ситуации, например, когда файл, который пытается прочитать пользователь, не существует.
- [x] Убедиться, что код написан чисто и легко читается, с соответствующими комментариями и документацией.

## Бонусное задание:

- Реализовать функцию, которая анализирует лог-файл и выводит обобщенную статистику, например, количество записей каждого уровня важности или самые часто встречающиеся ключевые слова.
- Добавить возможность работы с несколькими лог-файлами одновременно.
