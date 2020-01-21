# faq-django-database-gunicorn-nginx-docker

A simple FAQ system.

- [Windows Setup Instructions(Traditional Chinese)](https://hackmd.io/@Superdanby/BJicDitl8)

## Prerequisite

- `docker-compose`: version 3

### Docker Fedora Installation

1. `sudo dnf -y install dnf-plugins-core`
2. `sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo`
3. `sudo dnf install docker-ce docker-ce-cli containerd.io`

### Docker Daemon on Fedora

- Start once: `sudo systemctl start docker`
- Start on every boot: `sudo systemctl enable docker`

## Usage

1. Download `start.yml` and `.env.exmaple`, and put them in the same directory
2. [Edit `.env.exmaple`](https://github.com/Superdanby/faq-django-database-gunicorn-nginx-docker#env) and rename it to `.env`
3. `docker-compose -f start.yml up -d`
4. Go to [localhost](localhost) and it should be running

### Update

Update to the newest version requires rebuilding the images:

1. Stop the service: `docker-compose -f start.yml down`
2. Rebuild the images: `docker-compose -f start.yml build --no-cache`
3. Start the service: `docker-compose -f start.yml up -d`

## .env

| Variable | Default value | Description | Containers using the variable |
| -------- | ------------- | ----------- | ------------------- |
| `DB_TYPE` | '' | Supported values are `mariadb`(`mysql`), `postgres`(`postgresql`), should be specified even in development | `web` |
| `DEBUG` | `0` | Production: `0` / Development: `1` | `web` |
| `SECRET_KEY` | `yaaaaaaaaaaaaa!` | Change this to a hard-to-guess random string | `web` |
| `DJANGO_ALLOWED_HOSTS` | `localhost 127.0.0.1 [::1]` | the IPs/domain names that this Django site can be served | `web` |
| `DJANGO_SUPER_USER` | `yaaaaaaaaaaaaa!` | Default admin page username | `web` |
| `DJANGO_SUPER_PASSWORD` | `yaaaaaaaaaaaaa!` | Default admin page password | `web` |
| `DJANGO_SUPER_EMAIL` |  `yaaaaa@yaaa.yaa` | Email of the admin user | `web` |
| `HOST` | `db` | Domain name or IP of the database, use `127.0.0.1` instead of `localhost` in development | `web` |
| `PORT` | `` | Port of the database(`postgres`: `5432`, `mariadb`: `3306`) | `web` |
| `MYSQL_ROOT_PASSWORD` | `yaaaaaaaaaaaaa!` | Mariadb `root` password | `web` & `db` |
| `MYSQL_DATABASE` | `faqs` | Mysql default database | `web` & `db` |
| `POSTGRES_USER` | `yaaaaaaaaaaaaa!` | Postgres super account username | `web` & `db` |
| `POSTGRES_PASSWORD` | `yaaaaaaaaaaaaa!` | Postgres super account password | `web` & `db` |
| `POSTGRES_DB` | `faqs` | Postgres default database | `web` & `db` |

## Django Development Instructions

1. Clone this repository
2. Create your [`.env.dev`](https://github.com/Superdanby/faq-django-database-gunicorn-nginx-docker#env)
3. `source .env.dev && export $(cut -d = -f 1 .env.dev)`
4. In `start_[database].yml`, under `db:`, edit:
    ```yaml=
    db:
      ...
      # postgres
      env_file:
        - .env.dev
      ports:
        - 5432:5432
      ...

    db:
      ...
      # mariadb
      env_file:
        - .env.dev
      ports:
        - 3306:3306
      ...
    ```
5. `docker-compose -f start_[database].yml up -d db`
6. `python3 manage.py runserver`
7. If you need [static files and media files to be served](https://docs.djangoproject.com/en/3.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development), add `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)` after `urlpatterns` in `faq/urls.py`, and change `STATIC_ROOT` & `MEDIA_ROOT` in `faq/settings.py` to somewhere you have permission.

## Fork Instructions

1. Fork this repository
2. Clone your repository
3. Change the upstream urls:
   - In `start_[database].yml`: 2 urls in the value field of `context`
   - In `dockerfile`: 1 url after `RUN git clone`
   - In `nginx.dockerfile`: 1 url after `RUN curl`
4. Commit and push your changes
5. Remember to push your changes to the upstream repository and [update](https://github.com/Superdanby/faq-django-database-gunicorn-nginx-docker#update) it before starting the services.

## Windows Issues and Workarounds

1. [`postgres` docker image can't specify host volumes](https://github.com/docker/for-win/issues/445)
   - Use `mariadb` instead
2. [`mariadb` can't start with InnoDB: auto-extending data file ./ibdata1 is of a different size 0 pages](https://github.com/docker-library/mariadb/issues/95#issuecomment-407839431)
   - Add `--innodb-flush-method=fsync` to the `command` value under `db` in `start_mariadb.yml`
