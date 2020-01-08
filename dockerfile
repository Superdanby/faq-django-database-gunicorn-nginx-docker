FROM centos:8

RUN yum -y install python3-devel libpq-devel git gcc gettext

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/Superdanby/faq-django-postgres-gunicorn-nginx.git
WORKDIR /faq-django-postgres-gunicorn-nginx
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
