FROM centos:8

RUN yum install python3 libpq-devel
RUN python3 -m venv venv && source venv/bin/activate

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN git clone https://github.com/Superdanby/faq-django-postgres-gunicorn-nginx.git
WORKDIR /faq-django-postgres-gunicorn-nginx
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
