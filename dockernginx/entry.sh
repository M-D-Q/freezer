#!/bin/sh

/etc/init.d/fcgiwrap start
chmod 766 /var/run/fcgiwrap.socket
/usr/sbin/nginx -g "daemon off;"

