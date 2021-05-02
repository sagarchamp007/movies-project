movies-project

In psql terminal ->. 
create user moviescoll with password 'moviescoll';  
alter role moviescoll with superuser createdb createrole;  
CREATE DATABASE moviescolldb OWNER moviescoll;  

Connect using-> psql -d moviescolldb -U moviescoll. 

TO install ->. 
pip install -r requirements.txt. 

TO Run -  
python manage.py makemigrations. 
python manage.py migrate. 
python manage.py runserver. 


APIS ->.  
Import link in Postman. 
https://www.getpostman.com/collections/aa3eb1b423e779a5a714. 
