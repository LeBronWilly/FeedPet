# FeedPet
執行
```Python
python manage.py runserver
```

有更改model就要執行以下指令
```Python
python manage.py makemigrations
python manage.py migrate
```

偶爾上面的指令沒用時
1. 刪除該db.sqlite3 & app底下的migrations資料夾
2. 然後執行
```Python
python manage.py makemigrations [appname]
python manage.py migrate [appname]
```
