# lokmandjango

git clone https://github.com/lokmannhi/lokmandjango.git

make sure to have python3 install
python3 --version to check your version

you need to install using the command
pip install django djangorestframework

use this command for migration
python3 manage.py migrate

-- can skip if you want to --
if you want to create a super user
python manage.py createsuperuser
got to http://127.0.0.1:8000/admin/ to log in to you super user account

run the server with this command
python3 manage.py runserver
http://127.0.0.1:8000/

for test
python3 manage.py test inventory
