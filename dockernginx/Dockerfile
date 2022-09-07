FROM nginx
RUN apt update  
RUN apt install fcgiwrap python3 -y

COPY fastcgi_params /etc/nginx
COPY server.crt /etc/nginx/server.crt
COPY server.key /etc/nginx/server.key
COPY index.cgi  /srv/pythoncgi/index.cgi
COPY index.html /var/www/html/nginx/index.html
RUN rm /etc/nginx/conf.d/default.conf
COPY site_nginx.conf /etc/nginx/conf.d/default.conf
RUN rm -f /etc/nginx/nginx.conf
COPY  nginx.conf  /etc/nginx/nginx.conf



#EXPOSE 80:443
#ENTRYPOINT nginx -g 'daemon off;'

COPY entry.sh /
RUN chmod 755 /entry.sh
ENTRYPOINT ["./entry.sh"]


