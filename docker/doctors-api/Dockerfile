# Production ready docker file for the doctors list API service
# build with src as the context. Also used as the remote
# devcontainer for VSCode. 
#
# When building for production run `docker build --target prod...`

FROM python:3.9-slim as prod
ARG GID=1000
ARG UID=1000
COPY . /workspace
RUN groupadd -g $GID runner &&\
    useradd -m -u $UID -g $GID runner &&\
    pip install Django djangorestframework markdown django-filter
# the following line maybe removable in actual production with a production database so we don't need to import a yaml fixture
RUN pip install pyyaml 
WORKDIR /workspace
USER 1000:1000
# temporary startup procedure, in actual production there are numerous config and dependencies to setup
ENV DJANGO_SUPERUSER_PASSWORD="passalot"
ENV DJANGO_SUPERUSER_EMAIL="admin@example.com"
ENV	DJANGO_SUPERUSER_USERNAME="admin"
ENTRYPOINT [ "/bin/bash" ]
CMD ["-c", "python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser --noinput && python manage.py loaddata doctors.yaml && python manage.py runserver 0.0.0.0:8000"]
    

FROM prod as dev
USER root
RUN pip install autopep8 black yapf bandit flake8 mypy pycodestyle pydocstyle pylint pytest pylint-django &&\
    apt update && apt install -y git curl sqlite
USER 1000:1000