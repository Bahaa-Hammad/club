# IEEE 
# Overview

A content managment solution that helps university club manage their diffrent types of content. This version focuses on event planners and organizers to manage their events efficiently and effectively. It includes features such as event registration, guests management, event marketing, event management. Event managers can use the system to manage multiple events, such as seminars, conferences, field trips, and festivals. Each event can be pulished with dynamic agenda for guests to follow through out the event. It also provides valuable insights into event performance and helps to identify potential areas of improvement.

Generic bases is applicaple on diffrent types of university clubs, this version is being developed by collaborating with IEEE PSU Student Chapter. 

# Features
* Showcase Upcoming Events
* Archive Previous Events
* Manage Event Agendas
* Manage Event Images
* Manage Event Guests
* User Registration & Authenticaiton
* Admin Panel


# Tech Stack
Backend:
* Python
* Django
* Postgres (production), sqlite3  (devolopment)
* Pillow

Frontend:
* Bootstrap 5
* Django Page Templates
# Postgress Database Design 
![image](https://user-images.githubusercontent.com/89856041/221377833-06064eed-aabd-410e-baa2-0c098ed668c8.png)

# File Structure
```
│   .gitignore
│   db.sqlite3
│   manage.py
│
├───club
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│
│
├───events
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   │
│   ├───templates
│   │   └───events
│   │           event.html
│
├───landing_page
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───templates
│   │   └───landing_page
│   │           index.html
│
├───static
│   ├───assets
│   │   ├───css
│   │   │       main.css
│   │   │
│   │   ├───js
│   │   │       main.js
│   │   │
│   │   ├───scss
│   │   │       Readme.txt
│   │   │
│   │   └───vendor
│   │       ├───aos
│   │       │       aos.css
│   │       │       aos.js
│   │       │
│   │       ├───bootstrap
│   │       │   ├───css
│   │       │   │       bootstrap-grid.css
│   │       │   │       bootstrap-grid.css.map
│   │       │   │       bootstrap-grid.min.css
│   │       │   │       bootstrap-grid.min.css.map
│   │       │   │       bootstrap-grid.rtl.css
│   │       │   │       bootstrap-grid.rtl.css.map
│   │       │   │       bootstrap-grid.rtl.min.css
│   │       │   │       bootstrap-grid.rtl.min.css.map
│   │       │   │       bootstrap-reboot.css
│   │       │   │       bootstrap-reboot.css.map
│   │       │   │       bootstrap-reboot.min.css
│   │       │   │       bootstrap-reboot.min.css.map
│   │       │   │       bootstrap-reboot.rtl.css
│   │       │   │       bootstrap-reboot.rtl.css.map
│   │       │   │       bootstrap-reboot.rtl.min.css
│   │       │   │       bootstrap-reboot.rtl.min.css.map
│   │       │   │       bootstrap-utilities.css
│   │       │   │       bootstrap-utilities.css.map
│   │       │   │       bootstrap-utilities.min.css
│   │       │   │       bootstrap-utilities.min.css.map
│   │       │   │       bootstrap-utilities.rtl.css
│   │       │   │       bootstrap-utilities.rtl.css.map
│   │       │   │       bootstrap-utilities.rtl.min.css
│   │       │   │       bootstrap-utilities.rtl.min.css.map
│   │       │   │       bootstrap.css
│   │       │   │       bootstrap.css.map
│   │       │   │       bootstrap.min.css
│   │       │   │       bootstrap.min.css.map
│   │       │   │       bootstrap.rtl.css
│   │       │   │       bootstrap.rtl.css.map
│   │       │   │       bootstrap.rtl.min.css
│   │       │   │       bootstrap.rtl.min.css.map
│   │       │   │
│   │       │   └───js
│   │       │           bootstrap.bundle.js
│   │       │           bootstrap.bundle.js.map
│   │       │           bootstrap.bundle.min.js
│   │       │           bootstrap.bundle.min.js.map
│   │       │           bootstrap.esm.js
│   │       │           bootstrap.esm.js.map
│   │       │           bootstrap.esm.min.js
│   │       │           bootstrap.esm.min.js.map
│   │       │           bootstrap.js
│   │       │           bootstrap.js.map
│   │       │           bootstrap.min.js
│   │       │           bootstrap.min.js.map
│   │       │
│   │       ├───bootstrap-icons
│   │       │   │   bootstrap-icons.css
│   │       │   │   bootstrap-icons.json
│   │       │   │
│   │       │   └───fonts
│   │       │           bootstrap-icons.woff
│   │       │           bootstrap-icons.woff2
│   │       │
│   │       ├───glightbox
│   │       │   ├───css
│   │       │   │       glightbox.css
│   │       │   │       glightbox.min.css
│   │       │   │       plyr.css
│   │       │   │       plyr.min.css
│   │       │   │
│   │       │   └───js
│   │       │           glightbox.js
│   │       │           glightbox.min.js
│   │       │
│   │       ├───isotope-layout
│   │       │       isotope.pkgd.js
│   │       │       isotope.pkgd.min.js
│   │       │
│   │       ├───purecounter
│   │       │       purecounter_vanilla.js
│   │       │
│   │       └───swiper
│   │               swiper-bundle.min.css
│   │               swiper-bundle.min.js
│   │               swiper-bundle.min.js.map
│   │
│   └───images
│           oracleVist.jpg
│           oracleVist_FT8llM6.jpg
│           pjam8.jpg
│           pjam8_guI61Jx.jpg
│
├───templates
│       boilerplate.html
│
└───users
    │   admin.py
    │   apps.py
    │   forms.py
    │   models.py
    │   tests.py
    │   urls.py
    │   views.py
    │   __init__.py
    │
    ├───templates
    │   └───users
    │           login.html
    │           profile.html
    │           register.html
```

# Installation (Without docker)
* clone repo
* create a virtual environment and activate
* pip install virtualenv
```
virtualenv envname
```
```
envname\scripts\activate
```
* cd into project
```
$ pip install -r requirements.txt
```
# Running the project
* make the migrations
```
 $ python manage.py makemigrations
```
* Apply the migrations
```
 $ python manage.py migrate
```
* Create admin user
```
$ python manage.py createsuperuser
```
* Run unit testing
```
$ python manage.py test
```
* Run the project
```
 $ python manage.py runserver
```
* Now you can open http://localhost:8000 in your browser

# Future enhancement plans
* Implement blog managment

# How To run with docker

Development
Uses the default Django development server. 
```
$ docker-compose up -d --build
```
Test it out at http://localhost:8000. 

Production
Uses gunicorn + nginx.

Build the images and run the containers:
```
$ docker-compose -f docker-compose.prod.yml up -d --build
```
Test it out at http://localhost:1337. 

# Final Report 
https://docs.google.com/document/d/1FuBl4ddKi2MyzWrf69zwd5Cxo8L311mLWYzdabKhZPY/edit?usp=sharing
