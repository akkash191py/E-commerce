---

## Project Setup

Please follow bellow steps to setup the project.

1. Create virtual environment
   ```
   pip install virtualenv
   ```
2. Activate the virtual env
   ```
   venv/Scripts/activate
   ```
3. Install project dependencies
   ```
    pip install -r requirements.txt
   ```
4. Create .env file in the project directory and add following,
   ```
   DB_NAME=ecommerce_db
   DB_USER=root
   DB_PASSWORD=root
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DEBUG=True
   SECRET_KEY='django-insecure-8z$(#a7(3u9ozk5cu3u%0*x@hv9ts#m_qc6zefit+f1ro_j(gm'
   
   ```

5. Create django migrations
    ```
    python manage.py makemigrations ecomm_auth
	python manage.py makemigrations
    ```
6. Migrate the SQL changes
   ```
    python manage.py migrate
 
   ```
7. runserver
   ```
    python manage.py runserver
 
   ```
8. django admin username and password
   ```
    username=admin
    password=admin
 
   ```

---

---

