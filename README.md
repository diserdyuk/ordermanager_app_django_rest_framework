# ordermanager_app_django_rest_framework

Реализовать систему для управлением заказами в магазине техники. 
Представьте, что ваш клиент хочет автоматизировать свой бизнес в магазине техники, 
и вам нужно внедрить серверную часть для этой автоматизации.


В системе задействованы следующие участники:
1) Продавец-консультант
2) Кассир
3) Бухгалтер


Типичный вариант использования:
1) кассир получает заказ от клиента. В одном заказе может быть только один продукт
-> добавляет этот заказ в базу данных
2) продавец-консультант может видеть созданный заказ
-> обрабатывает его и затем изменяет его статус на «выполнено»


После этого
1) кассир может сгенерировать счет
2) принять оплату от клиента и изменить статус заказа на «оплачен»


В любое время бухгалтер может видеть все заказы, их статусы, дату, скидку и тд.
Бухгалтер указывает промежуток дат по которым необходимо вывести данные о заказах.
Например: показать все заказы с 01.07.2019 до 31.07.2019

Продукты имеют название, цену и дату создания. 
В системе должен быть реализован механизм начисления скидок для товаров. 
Если дата создания продукта больше одного месяца от текущей даты, 
то на него должна быть предоставлена скидка 20%.

Счет должен содержать информацию о товаре (название, цена) и дату создания заказа и
дату создания счета.


ТРЕБОВАНИЯ К ОФОРМЛЕНИЮ
1) система должна быть выполнена в виде REST API (либо GraphQL)
2) в проекте должны быть фикстуры для продуктов
3) необходимо предоставить Postman коллекцию (GraphQL Playground) со всеми ендпоинтами, 
либо документацию к реализованным endpoints в любом удобном для вас виде
4) Код должен соответствовать общепринятым стилевым и организационным
стандартам действующим для выбранных вами языков и технологий
5) по возможности код должен сопровождаться разумными комментариями,
юнит-тестами, прочими инструкциями



Для запуска проекта


1) установить виртуальное окружение
$ virtualenv venv


2) запустить venv
$ source venv/bin/activate


3) установить библиотеки
requirements.txt


4) сделать миграции
$ python manage.py makemigrations
$ python manage.py migrate


5) создать суперюзера
$ python manage.py createsuperuser


6) запусить локальный сервер
$ python manage.py runserver


7) перейти в админку 
http://127.0.0.1:8000/admin


8) в админке создать, несколько
продуктов
заказов
кассиров


9) октрыть в браузере
http://127.0.0.1:8000/api
