# FeedPet
##環境
<br>
Python 3.7.4 (此版本之上可行)
<br>
Django 2.2.7 (限定此版本)
<br>

##安裝
```Python
pip install Pillow
pip install requests
pip install django-model-utils
pip install djangorestframework
pip install geocoder
pip install geojson
```

##有更改model就要執行以下指令
```Python
python manage.py makemigrations
python manage.py migrate
```

##執行
```Python
python manage.py runserver
```

##偶爾上面的指令沒用時
1. 刪除db.sqlite3 & 該app底下的migrations資料夾
2. 然後執行
```Python
python manage.py makemigrations [appname]
python manage.py migrate [appname]
```


##匯入飼料open data
http://localhost:8000/feed/import_feed
(此部分程式碼已修正完畢，但政府OpenData那裡出了問題，待政府修正)
<br>
##匯入旅館open data
http://localhost:8000/hotel/import_hotel
<br>
