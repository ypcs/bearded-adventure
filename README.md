bearded-adventure
===================================================
Bearded Adventure is ....

This package includes Django-based (master) server. You also need client 
tools for slaves, available as separate package. (In future!)


## Getting started
Currently developed in Python Virtualenv, `apt-get install 
python-virtualenv python-pip virtualenvwrapper` might be required, 
depending on your environment.

Fetch code from GitHub.

    git clone https://github.com/ypcs/bearded-adventure
    cd bearded-adventure

Create new Python virtualenv.    

    mkvirtualenv bearded

Install Python requirements.
    
    pip install -r requirements.txt

Configure database.

    cd bearded_adventure
    python manage.py syncdb
    python manage.py migrate
    
Run testserver.

    python manage.py runserver
