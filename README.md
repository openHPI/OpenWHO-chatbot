# KI-Campus Chatbot

## Training of the Model 

```sh
    cd openWHO/
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
    docker-compose -f docker-compose.yml -p openwho up --build
```
