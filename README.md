# openWHO Chatbot v2

## Training of the Model 

```sh
    cd rasa/openWHO_{LANGUAGE}/
    rasa train
```

## Usage

### Start the Rasa Server

```sh
    rasa run --enable-api
```

### Start the Action Server

```sh
    cd actions/
    rasa run actions
```

## Docker

In the outer project structure run:

```sh
    docker-compose up --build
```


### Docker Compose (en)

```sh
    docker-compose -f docker-compose_en.yml -p openWHO_en up --build
```

### Docker Compose (es)

```sh
    docker-compose -f docker-compose_es.yml -p openWHO_es up --build
```

### Docker Compose (zh)

```sh
    docker-compose -f docker-compose_zh.yml -p openWHO_zh up --build
```