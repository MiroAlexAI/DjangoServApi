### Для запуска -
 В папке \Dj_server_mir> 
 ввести в Терминале
 python manage.py runserver

Или запустить файл
RUN SERVER.bat


# DjangoServApi
Test project 

### Пример работы в браузере
![image](https://github.com/MiroAlexAI/DjangoServApi/assets/126348122/9f4dba65-c9dc-4b84-ae7c-20ada6f194bb)

### Запрос к API

>curl -X POST -H "Content-Type: application/json" -d '{"username": "newuser1", "password": "newpass123", "email":"newtwst@mail.com"}' >http://127.0.0.1:8000/api/create_user/


### URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome, name='welcome'),
    path('api/', include('myapp.urls')),
]

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
]

