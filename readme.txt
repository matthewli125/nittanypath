CMPSC431W Project Phase 2 README

Please read this document to understand how I completed the tasks of populating the database and creating the login page.
All dependencies and packages are contained in a virtual environment in this project.

DATABASE

- I used excel to process the raw data given to us into schema, and saved them as CSV files individually. The individual
  CSV files can be found in dataFiles, and all the sheets and scratchfiles can be found in "431 project database".xlsx.
- Excel provides a lot of simple tools that can remove duplicates, match key-value pairs, etc. VERY quickly, making it
  a great tool for cleaning the data.

- I used SQLite3 as the database backend with django. I first wrote django models for the schemas in ntnyPth/models.py.
- At first I tried writing a django script in load_data.py, but decided it was easier to write raw sql queries in the
  PyCharm database console, given all the insertions needed and integrity constraints.
- I generated VALUE tuples using the script in create_stmts.py.


LOGIN PAGE

- Django provides excellent login, authentication, and password management support, making this process a relative breeze.
- I followed a tutorial from https://learndjango.com/tutorials/django-login-and-logout-tutorial for a basic login page
  implementation.
- There are three html files: login.html, base.html, and home.html. login.html is in a subdirectory "registration".
  -  home.html extends base.html to create a basic homepage that displays different things based on if the user is
     logged in or not.
  - login.html is the login page that provides a form with username and password.

- Users and passwords were extracted from the students and professors tables, and passwords are hashed automatically by
  django and stored in the auth_user table. Professors are also given a staff status.


HOW TO RUN
- Open this project in PyCharm. Click the Run button. Alternatively, run "python manage.py runserver".
- Using PyCharm is necessary because django exists in a venv specific to this project.
- The terminal will display a uri that you can connect to in a browser.
- To connect to the admin site and view the database in the django GUI, add "/admin" to the uri.
  - example: "https://127.0.0.1:8000/admin"
  - admin username: admin
  - admin password: 123456