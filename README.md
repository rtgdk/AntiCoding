# AntiCoding
App for anticoding event
# Installing and running up the application (For ubuntu and windows)
You need to have python(https://www.python.org/downloads/) and pip(https://pip.pypa.io/en/stable/installing/) installed.

Change the directory to the root folder(anticoding using `cd` commands)
(Don't copy "`")
1. `pip install -r requirements.txt`	
2. `python manage.py migrate`
3. `python manage.py createsuperuser` and enter details of the administrator. Using the credentials you can login as admin ('/admin'/).
4. `python manage.py runserver` , this will start the application on 127.0.0.1:8000/app/ or localhost:8000/app/. This won't allow other computers to connect to the server.
5. Or you can also `python manage.py runserver <IP address>:<port>` . You can find the IP address using ipconfig(Windows)/ifconfig(Ubuntu). Port can be anything.
	Eg: `python manage.py runserver 192.168.0.1:8900`. This will allow other computers to connect to the server using the same ip address and port(192.168.0.1:8900).
6. Or you can simply run `python manage.py runserver 0.0.0.0:8000`. And other computers to connect to the server using the server ip address and port as 8000.(You can find the IP address using ipconfig(Windows)/ifconfig(Ubuntu)) 
