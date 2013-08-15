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


## Setting up Nginx reverse proxy
Update your Nginx config:

    location / {
        proxy_pass http://127.0.0.1:8000/;
        proxy_redirect     off;
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
    }
                    
    # TODO: Add config for WebSocket proxy.
