from drf_yasg import openapi

swagger_get_book = {
'operation_id': 'book_get',
    'methods': ['GET'],
    'manual_parameters': [
        openapi.Parameter('token', openapi.IN_PATH, "token пользователя", type=openapi.TYPE_STRING, required=True),
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

