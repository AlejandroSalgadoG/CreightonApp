Application for Creighton model

### Docker commands

    docker build -t <repo>:<tag> .
    docker images
    docker container ls -a
    docker run --rm -it <image> <command>
    docker exec -it <container> <command>

### Docker compose commands

    docker-compose run --rm app
    docker-compose run --rm app sh
    docker-compose run --rm app sh -c <command>
    docker-compose up

### Django commands

    docker-compose run --rm app sh -c "django-admin startproject <name> ."
    docker-compose run --rm app sh -c "python manage.py test"
    docker-compose run --rm app sh -c flake8
