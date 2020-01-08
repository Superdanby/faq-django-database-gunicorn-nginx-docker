FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
RUN apt-get update
RUN apt-get -y install curl
RUN curl https://raw.githubusercontent.com/Superdanby/faq-django-postgres-gunicorn-nginx/master/nginx.conf -o /etc/nginx/conf.d/nginx.conf