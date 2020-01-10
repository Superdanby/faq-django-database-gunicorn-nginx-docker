FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
RUN apt-get update
RUN apt-get -y install curl
RUN curl https://raw.githubusercontent.com/Superdanby/faq-django-database-gunicorn-nginx-docker/master/nginx.conf -o /etc/nginx/conf.d/nginx.conf
