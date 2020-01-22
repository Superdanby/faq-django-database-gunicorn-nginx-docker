FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
RUN apt-get update
RUN apt-get -y install curl
RUN curl https://raw.githubusercontent.com/Superdanby/faq-django-database-gunicorn-nginx-docker/master/nginx.conf -o /etc/nginx/conf.d/nginx.conf
RUN mkdir /etc/nginx/snippets
RUN curl https://raw.githubusercontent.com/Superdanby/faq-django-database-gunicorn-nginx-docker/master/self-signed.conf -o /etc/nginx/snippets/self-signed.conf
RUN curl https://raw.githubusercontent.com/Superdanby/faq-django-database-gunicorn-nginx-docker/master/ssl-params.conf -o /etc/nginx/snippets/ssl-params.conf
RUN curl https://raw.githubusercontent.com/Superdanby/faq-django-database-gunicorn-nginx-docker/master/ssl.sh -o /ssl.sh
RUN chmod +x /ssl.sh
