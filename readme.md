# Консольное приложение для работы с лог-файлами

## Описание задачи:

Ваша задача - создать консольное приложение на Python, которое будет анализировать лог-файлы. Предположим, что каждая строка лог-файла имеет следующий формат: дата и время события, уровень важности (INFO, WARNING, ERROR), и сообщение об ошибке или событии.

## Приложение должно поддерживать следующие функции:

 Чтение лог-файла: Приложение должно прочитать лог-файл и отобразить его содержимое.
 Фильтрация по уровню важности: Пользователь может указать уровень важности (INFO, WARNING, ERROR), и приложение должно отобразить только записи с этим уровнем важности.
 Поиск по ключевым словам: Пользователь может ввести ключевое слово, и приложение должно отобразить все записи, содержащие это слово.
 Сортировка записей: Пользователь может выбрать, сортировать ли записи по дате и времени в прямом или обратном порядке.

## Основные требования:

Реализуйте функционал с использованием встроенных функций Python для работы с файлами.
Обработайте возможные исключительные ситуации, например, когда файл, который пытается прочитать пользователь, не существует.
Убедитесь, что код написан чисто и легко читается, с соответствующими комментариями и документацией.

## Бонусное задание:

Реализуйте функцию, которая анализирует лог-файл и выводит обобщенную статистику, например, количество записей каждого уровня важности или самые часто встречающиеся ключевые слова.
Добавьте возможность работы с несколькими лог-файлами одновременно.
