#!/bin/sh

# constantes
HOST=10.5.0.6
LOGIN=test
PASSWORD=test
PORT=21


# le transfert
ftp -i -n $HOST $PORT << END_SCRIPT
quote USER $LOGIN
quote PASS $PASSWORD
cwd /nginx_share
put index.cgi
quit
END_SCRIPT

