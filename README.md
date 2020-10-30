# Support Bot

## Architecture

[Rasa](https://rasa.com/) is an open source platform for building chat bots. It consists of two major parts: the Rasa Core and the Rasa NLU. 

## Setup

### Training

1. Update config.yml with project to import. For example for openWHO:

```
imports:
- projects/openWHO
```

2. Start the training and state models folder for current project:

```sh
    rasa train --out models/openWHO
```

### Usage

<!-- 2. Inside /rasa start Action Server (only for openSAP)

```sh
    rasa run actions -vv --actions actions.openSAP.account
``` -->

Inside /rasa start rasa with models-folder for current project:

```sh
    rasa run -vv -m projects/openWHO/models --enable-api
```

## Docker

1. Inside /rasa create the image

```sh
    docker image build -t openwho:1.0 .
```

2. Start docker-compose

```sh
    docker-compose -p openwho up
```
