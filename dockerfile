FROM centos:8

RUN yum -y install python3-devel libpq-devel mysql-devel git gcc gettext

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/Superdanby/faq-django-database-gunicorn-nginx-docker.git
WORKDIR /faq-django-database-gunicorn-nginx-docker
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
