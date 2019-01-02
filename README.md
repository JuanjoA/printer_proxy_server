# printer_proxy_server

A Flask server that provides a JSON-RPC interface to an Eltron 2844 CTP label printer, protected by SSL and Basic HTTP Authentication. It is designed for use with [printer_proxy](https://github.com/ryepdx/printer_proxy).

Assumes the printer is named "zebra" by default.


## Install:

    $ git clone git@github.com:ryepdx/printer_proxy_server.git
    $ cd printer_proxy_server
    $ virtualenv --python=python2.7 venv27
    $ source venv27/bin/activate
    $ pip install -r requirements.txt

## Create certificates (server.crt and server.key):

    $ openssl genrsa -des3 -out server.pass.key 2048
    $ openssl rsa -in server.pass.key -out server.key 
    $ openssl req -new -key server.key -out server.csr
    $ openssl x509 -req -sha256 -days 999 -in server.csr -signkey server.key -out server.crt

## Usage:

    $ python app.py

## Usage for printers not named "zebra":

    $ python app.py -d "Eltron 2844"

## Adding users

    $ python
    
    >>> from app import add_user
    >>> add_user("user", "password")
    >>> exit()

## Removing users

    $ python
    
    >>> from app import delete_user
    >>> delete_user("user")
    >>> exit()

## Accessing the user database directly

    $ sqlite3 users.db
    
    sqlite> select * from users;

    user|494c884325be4798032547ee6525d03d8bf96977d623a2ebafa0095bf5b194dd|4f1a6f06-c8fd-4526-a375-986fa298c36b

    sqlite> .q


## Links

    https://localhost:8443/api/browse/#/   (GET)
    https://localhost.santafixie.com:8443/api/  (JSON)

## More

For unix systems this app uses _lpr -Pprinter_name_ command to print (_helpers/zebra.py_).