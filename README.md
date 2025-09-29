QA API Service
Простое приложение для вопросов и ответов, построенное на FastAPI с асинхронной работой с базой данных PostgreSQL.

🚀 Функциональность
Вопросы
GET /questions/ - Получить список всех вопросов с ответами

POST /question_create/ - Создать новый вопрос

GET /questions/{question_id} - Получить конкретный вопрос по ID

DELETE /questions/{question_id} - Удалить вопрос и все связанные ответы

Ответы
POST /questions/{question_id}/answers/ - Создать ответ на конкретный вопрос

GET /answers/{answer_id} - Получить ответ по ID

DELETE /answers/{answer_id} - Удалить ответ

🛠 Технологии
FastAPI - веб-фреймворк

SQLAlchemy 2.0 - ORM с асинхронной поддержкой

PostgreSQL - база данных

AsyncPG - асинхронный драйвер для PostgreSQL

Pydantic - валидация данных

Docker - контейнеризация

🏃‍♂️ Запуск приложения
Предварительные требования:

Docker и Docker Compose
Python 3.8+

Запуск с Docker
Соберите и запустите контейнеры:

docker-compose up --build

Приложение будет доступно по адресу: http://localhost:8000
Документация API: http://localhost:8000/docs

📊 Модели данных
Question (Вопросы)

id - уникальный идентификатор
text - текст вопроса
created_at - дата создания
answers - список связанных ответов

Answer (Ответы)

id - уникальный идентификатор
question_id - ID связанного вопроса
user_id - UUID пользователя
text - текст ответа
created_at - дата создания

🔧 Настройка базы данных
Основная база данных:

URL: postgresql+asyncpg://admin:root@db:5432/Question_Answer_db
Пользователь: admin
Пароль: root
База данных: Question_Answer_db

📚 API Endpoints

Вопросы

Метод	Endpoint	Описание
GET	/questions/	Все вопросы
POST	/question_create/	Создать вопрос
GET	/questions/{id}	Вопрос по ID
DELETE	/questions/{id}	Удалить вопрос

Ответы

Метод	Endpoint	Описание
POST	/questions/{id}/answers/	Ответ на вопрос
GET	/answers/{id}	Ответ по ID
DELETE	/answers/{id}	Удалить ответ

💡 Особенности

Асинхронность - все операции с БД выполняются асинхронно
Автоматическая документация - Swagger UI доступен по /docs
Каскадное удаление - при удалении вопроса удаляются все ответы
Валидация данных - через Pydantic схемы
UUID пользователей - автоматическая генерация идентификаторов

🐛 Логирование

Приложение использует logging с уровнем INFO для отслеживания операций.
