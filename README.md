# Онлайн магазин

## ДЗ 23.1. Права доступа

### Выполнено
- Созданы две группы: модератор для каталога и контент-менеджер для блога.
  Созданы два пользователя к этим группам (прописано в команде create_groups_and_stuff)

- Для Каталога разграничены права доступа:
  - Просматривать каталог и отдельно продукты может любой пользователь, в том числе не авторизованый.
    - У неавторизованного пользователя отображаются только опубликованные продукты
    - У авторизованного пользователя отображаются опубликованные продукты и те, которые создал этот пользователь.
    - У модератора отображаются все продукты.
  - Создавать новый продукт может только авторизованый пользователь.
  - Доступно редактирование продуктов:
    - Авторизованный пользователь может редактировать созданные им продукты (кроме поля публикации).
    - Модератор может редактировать только поля "описание", "категория" и "публикация".

- Для Блога разграничены права доступа:
  - Просматривать блог и отдельные статьи может любой пользователь, в том числе не авторизованый.
    - У неавторизованного пользователя отображаются только опубликованные статьи.
    - У авторизованного пользователя отображаются опубликованные статьи и те, которые создал этот пользователь.
    - У менеджера отображаются все статьи.
  - Создавать новыю статьи может только авторизованый пользователь.
  - Доступно редактирование статей:
    - Авторизованный пользователь может редактировать созданные им статьи (кроме поля публикации).
    - Менеджер может редактировать все поля.
  - Удалить статью может только менеджер или пользователь, который ее создал 


### Выполнено ранее

## ДЗ 22.2. Аутентификация

### Выполнено
- Создано приложение для работы с пользователем.
  Авторизация реализована по электронной почте.
  Из стандартных полей убран "логин", добавлены поля
  "аватар", "номер телефона", "страна".

- Реализован функционал аутентификации:
  - регистрирация по почте и паролю,
  - верификация почты через отправленное письмо,
  - авторизация,
  - восстановление пароля на автоматически сгенерированный.

- Реализован функционал редактирования профиля пользователя.

- Закрыта возможность редактирования и добавления новых продуктов и статей
  для неавторизованных пользователей.

- Для авторизованных пользователей оставлена возможность
  созданная статья или продукт, новые сущности "привязываются"
  к пользователю автоматически. 

#### ДЗ 22.1. Формы

### Выполнено
- В приложение catalog добавлены формы для моделей
  Product (продукт), UserQuestion (вопросы со страницы контактов).
  Изменена возможность создавать новые продукты на версию
  с использованием созданных форм. Реализовано ограничение на вводымые данные.

- Реализована модель Harvest (поставки),
  относительно ТЗ изменено название модели с "версии" на "поставки" 
  и пполе "название версии" заменено на "дату сборка урожая"
  (как более подходящее к содержимому магазина).

- В список продуктов выведена дата сбора урожая текущей поставки (при наличии).

- При изменении продукта реализован вывод информации по всем поставкам этого продукта
  с возможностью перехада на страницы для изменения поставки или создания новой. 

- Добавлена ограничение: у продукта может быть только одна текущая поставка. 

#### ДЗ 21.1. fbv и cbv

- Контроллеры в приложении catalog переведены с fbv на cbv 

- Добавлено новое приложение blog (см. в главном меню пункт блог)
  В приложении добавлена модель согласно ТЗ, реализован CRUD для этой модели.
  Создание статьи см. в конце списка статей.

- Реализован дополнительный функционал:
  - счетчик просмотров статей
  - отображение только тех статей, которые имеют статус "опубликовано"
  - динамически формируется slug при создании новой статьи
  - после создания и редактирования статьи идет перенаправление 
    на страницу с просмотром этой статьи.
  
- Реализована отправка письма, когда количество просмотров
  у статьи достигает 100.

#### ДЗ 20.2. Шаблонизация

- Создана страница с отображением информации по одному товару 

- Товары и категории выводятся в циклах

- Выделены базовый шаблон и подшаблон для навигации.
  
- Реализована подгрузка изображений.
  Формирование пути реализовано с помощью шаблонного тега. 
  
- Добавлен функционал создания нового продукта через форму на странице


#### ДЗ 20.1. Работа с ORM в Django

- Создана и подключена БД django_store, в настройках добавлены MEDIA 

- Созданы модели Product, Category. Модели перенесены в БД

- Настроена админка для моделей
  
- Созданы фикстуры для заполнения БД (data.json).
  Создана команда (fill_from_json) для заполнения БД с предварительной очисткой.
  
- Добавлена подгрузка данных в шаблоны из БД (категории, продукты, контакты)

#### ДЗ 19.2. Знакомство с Django
- Создан Django-проект

- Создано приложение catalog

- Сверстаны 2 страницы: домашняя и контакты.

  - Страницы расположены в catalog/templates/catalog
  - Пользовательские стили и картинки расположены в
  catalog/static/catalog

- Реализованы контроллеры для отображения созданных страниц

- Прописаны url-ы для отображения страниц внутри приложения 
и подключены во внешнем файле url-ов  

- Данные, отправляемые из формы на странице contacts
выводятся в консоль