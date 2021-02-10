from drf_yasg import openapi

# Документация для книг

swagger_get_book = {
    'operation_id': 'book_get',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter(
            'token',
            openapi.IN_PATH,
            "token пользователя",
            type=openapi.TYPE_STRING,
            required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернёт список книг",
            examples={
                "application/json": {
                    "books": [
                        {
                            "id": 1,
                            "name": "Свидетелей не будет",
                            "author_name": "Джеймс Хедли Чейз",
                            "status": "in_progress"
                        },
                        {
                            "id": 2,
                            "name": "Занятие для мужчин",
                            "author_name": "Джеймс Хедли Чейз",
                            "status": "read"
                        }
                    ]
                }
            }
        ),
        500: openapi.Response(
            description="Пустое поле с токеном",
            examples={
                "application/json": {'error': 'token is empty'}
            }
        ),
        404: openapi.Response(
            description="Пользователь с таким токеном не найден",
            examples={
                "application/json": {'error': 'user not found'}
            }
        )
    },
    'tags': ['book']
}
 
swagger_add_book = {
    'operation_id': 'book_add',
    'methods': ['POST'],
    'manual_parameters': [
        openapi.Parameter(
            'token',
            openapi.IN_PATH, 
            "token пользователя",
            type=openapi.TYPE_STRING,
            required=True),
        openapi.Parameter(
            'name',
            openapi.IN_PATH, 
            "Название книги",
            type=openapi.TYPE_STRING,
            required=True),
        openapi.Parameter(
            'author_name',
            openapi.IN_PATH, 
            "Автор книги",
            type=openapi.TYPE_STRING,
            required=True),
        openapi.Parameter(
            'status',
            openapi.IN_PATH, 
            "Прогресс",
            type=openapi.TYPE_STRING,
            required=True),
    ],
    "responses": {
        201: openapi.Response(
            description="Вернёт добавленную книгу",
            examples={
                "application/json": {
                    "book": {
                        "id": 3,
                        "name": "Двойная сдача",
                        "author_name": "Джеймс Хедли Чейз",
                        "status": "not_read"
                    }
                }
            }
        ),
        404: openapi.Response(
            description="Пользователь с таким токеном не найден, либо книга не найдена",
            examples={
                "application/json": [
                    {'error': 'user not found'},
                    {'error': 'not found book'}
                ]
            }
        ),
        500: openapi.Response(
            description="Одно или несколько обязательных полей не были заполнены",
            examples={
                "application/json": [
                    {'error': 'token is empty'},
                    {'error': 'name is empty'},
                    {'error': 'author_name is empty'},
                    {'error': 'status is empty'},
                ]
            }
        ),
    },
    'tags': ['book'],
}

swagger_update_book = {
    'operation_id': 'book_update',
    'methods': ['PUT'],
    'manual_parameters': [
        openapi.Parameter(
            'token',
            openapi.IN_PATH, 
            "token пользователя",
            type=openapi.TYPE_STRING,
            required=True),
        openapi.Parameter(
            'id',
            openapi.IN_PATH, 
            "ID книги",
            type=openapi.TYPE_INTEGER,
            required=True),
        openapi.Parameter(
            'name',
            "Название книги",
            type=openapi.TYPE_STRING,
            required=False),
        openapi.Parameter(
            'author_name',
            "Автор книги",
            type=openapi.TYPE_STRING,
            required=False),
        openapi.Parameter(
            'status',
            "Прогресс",
            type=openapi.TYPE_STRING,
            required=False),
    ],
    "responses": {
        200: openapi.Response(
            description="Вернёт обновлённую книгу",
            examples={
                "application/json": {
                    "book": {
                        "id": 3,
                        "name": "Двойная сдача",
                        "author_name": "Джеймс Хедли Чейз",
                        "status": "not_read"
                    }
                }
            }
        ),
        404: openapi.Response(
            description="Пользователь с таким токеном не найден, либо книга не найдена",
            examples={
                "application/json": [
                    {'error': 'user not found'},
                    {'error': 'not found book'}
                ]
            }
        ),
        500: openapi.Response(
            description="Одно или несколько обязательных полей не были заполнены",
            examples={
                "application/json":[
                    {'error': 'token is empty'},
                    {'error': 'id is empty'},
                ]
            }
        ),
    },
    'tags': ['book']
}

swagger_delete_book = {
    'operation_id': 'book_delete',
    'methods': ['DELETE'],
    'manual_parameters': [
        openapi.Parameter(
            'token',
            openapi.IN_PATH,
            "token пользователя",
            type=openapi.TYPE_STRING,
            required=True),
            openapi.Parameter(
            'id',
            openapi.IN_PATH, 
            "ID книги",
            type=openapi.TYPE_INTEGER,
            required=True),
    ],
    'responses': {
        200: openapi.Response(
            description="Вернёт строку об успешном удалении",
            examples={
                "application/json": {
                   "success": "book 'Свидетелей не будет' was deleted"
                }
            }
        ),
        500: openapi.Response(
            description="Одно или несколько обязательных полей не были заполнены",
            examples={
                "application/json": [
                    {'error': 'token is empty'},
                    {'error': 'id is empty'},
                ]
            }
        ),
        404: openapi.Response(
            description="Пользователь с таким токеном не найден, либо книга не найдена",
            examples={
                "application/json": [
                    {'error': 'user not found'},
                    {'error': 'not found book'}
                ]
            }
        )
    },
    'tags': ['book']
}

# Документация для работы с пользователем
swagger_register = {
    
}

swagger_login = {

}

swagger_update_user = {
    
}

swagger_delete_user = {
    
}
