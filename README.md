# openWHO Chatbot v2

## Training of the Model 

```sh
    cd rasa/openWHO/
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
