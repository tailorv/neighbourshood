# AREA51 - NEIGHBOURHOOD

## Description
 Application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.


![HOME PAGE](screenshots/home.png)

### HOME PAGE

### PROJECTS 

# User Stories


## As a user of the application I should be able to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

### System Features
#### Feature 
* NeighbourHood class:

* A neighborhood class with the following properties:

1. Neighbourhood Name
2. Neighborhood location
3. Occupants Count
4. Admin Foreign key

Some of the methods you will need to implement are:

* User class
* A user class with the following properties;

1. Name.
2. Id.
3. Neighborhood id foreign key
4. Email address

* Business class
* A business class with the following properties;

1. Business name
2. User foreign key
3. Neighborhood id foreign key
4. Business email address.
5. The Methods we will create are:


* Business search
* A business search functionality where users can search for businesses in their area.

* Admin Dashboard
* A dashboard that you will use to manage the different users.

* Authentication system
* A solid authentication system that allows users to sign in or register into the application before using it. When a user registers with this application they should receive a confirmation email.

## User environment

Application should be accessible to users on both desktop and mobile formats. The application is responsive to different screen sizes.

# Setup / Installation Requirements

## (A) Technologies Used
- Python 3.8
- Django 3.2
- Postgres Database
- UI-BOOTSTRAP
- Heroku

### (B) Step By Step Process

1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd instaratings`
4. Create a virtual environment with `virtualenv virtual` or try `python3 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE instaratings
```
9. Check the database informatioin in `/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instaratings',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_PASSWORD*,
    }
}
```
10. Run `./manage.py runserver` or `python3.8 manage.py runserver` to run the application

## Support and Contacts
* EMAIL:
 * maxwellmuthomijr@gmail.com

## LICENSE

{MIT License

Copyright (c) 2021

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. } Copyright (c) {2021} 
{ Maxwell Munene}
