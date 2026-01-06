cd C:\Users\Scythe\Desktop\testbank
call venv\Scripts\activate
waitress-serve --host=0.0.0.0 --port=8000 capstone.wsgi:application