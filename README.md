bearded-adventure
===================================================
Bearded Adventure is ....

This package includes Django-based (master) server. You also need client 
tools for slaves, available as separate package. (In future!)

## Why Bearded Advanture?
It was name that GitHub repository name generator gave us! 


## Getting started

Fetch code from GitHub.

    git clone https://github.com/ypcs/bearded-adventure
    cd bearded-adventure

Optional: Setup Vagrant box for development.

    apt-get install vagrant
    vagrant up # (in directory bearded-adventure)
    vagrant ssh

Create new Python virtualenv. If you prefer not using virtualenv, see 
requirements.txt for required Python packages (& supported versions).

    apt-get install python-virtualenv python-pip virtualenvwrapper
    source /etc/bash_completion.d/virtualenvwrapper # might be needed (to get virtualenvwrapper working w/o logout)
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
