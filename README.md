# Django matchmaker

DESCRIPTION OF THE PROJECT @jotapalas

## Local environment

### Prerequisites
This project is based on Docker containers, so you need to install **docker**, and **docker-compose**.

It is not necessary any concrete OS, but, all is easier with Linux (if you pretend to program).

Also, you must have ports **80** and **10001** free or modify the env file.

### Configuration
You don't have to configure the project if you don't want it. By default, it will work just deploying it. But, you can configure some things if you are brave.

<p align="center">
    <img src="https://media3.giphy.com/media/YTIzbJzeExuLK/source.gif">
</p>
By default, in the .env you can find some interesting variables, like for example the default backend super user:

```bash
SUPERUSER_NAME
SUPERUSER_PASSWORD
SUPERUSER_MAIL
```

And also the postgres variables:

```bash
POSTGRES_PASSWORD
POSTGRES_DB
EXTERNAL_PORT
```

If you pretend to use this in a production environment or even in your local but open the router ports to serve it, we encourage you to modify these values if you don't want to be exposed to guys like him:

<p align="center">
    <img src="https://media1.tenor.com/images/cf133d0a2e3c724ee88d5d08545df716/tenor.gif">
</p>

### Run the project

Run the project to execute on local if you have docker and docker-compose is extremely easy, just go with a terminal (even windows has cmd) to the project root and just execute the following lines 

```bash
docker-compose up --build -d
```

It will start to deploy all the containers in your local network.

After the docker-compose up ends (if you are using -d option in the command), you should wait a couple of seconds until it really works. You can see the Django logs using:

```bash
docker logs --tail 50 -f matchmaker_backend
```
