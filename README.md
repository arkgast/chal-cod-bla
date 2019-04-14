# Blackouts

## Make it run

    $ mkdir c4v
    $ cd c4v
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ git clone https://github.com/arkgast/chal-cod-bla
    $ cd chal-cod-bla
    $ pip install -r requirements.txt
    $ export FLASK_APP=main.py
    $ flask run
