# Sherlock

Welcome to Sherlock project. Sherlock is a movie recommendation microservice written in Flask.

Below steps can be executed on any unix like system. I will use ubuntu deployed on [O'Reilly's sandbox](https://learning.oreilly.com/scenarios/ubuntu-sandbox/9781492062837) (alternatively you could use [Katacoda's playground](https://www.katacoda.com/courses/ubuntu/playground2004)). Once the sandbox/playground is ready, execute instructions specified in below sections.

## Setup SSH key

Create ssh key and add it to GitHub's [SSH keys](https://github.com/settings/keys) settings.

```bash
ssh-keygen
cat ~/.ssh/id_rsa.pub
```

## Installation

```bash
# Cloning the source code
git clone https://github.com/ldynia/flask-sherlock.git
cd flask-sherlock

# Building and running docker container
docker build --tag flask-sherlock --build-arg FLASK_DEBUG=True .
docker run --detach --name sherlock --publish 80:8080 --rm flask-sherlock
docker ps
```

## API

```bash
curl "http://localhost/api/v1/movies/recommend?title=Kingpin"
curl "http://localhost/api/v1/movies/recommend?title=Lost%20in%20Translation"
```

## Testing

Unit test

```bash
docker exec sherlock pytest
```

Code coverage

```bash
docker exec sherlock coverage run -m pytest
docker exec sherlock coverage report
```

## Debug

```bash
{
    docker stop sherlock;
    docker build --no-cache --tag flask-sherlock $PWD;
    docker run --rm --detach --name sherlock --publish 80:8080 --volume $PWD/app:/app flask-sherlock;
}
```