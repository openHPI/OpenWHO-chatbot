FROM rasa/rasa:latest-full

COPY config.yml /app/config.yml
COPY openHPI_de/domain.yml /app/openHPI_de/domain.yml
COPY credentials.yml /app/credentials.yml
COPY endpoints.yml /app/endpoints.yml
COPY data/openHPI_de/* /app/data/openHPI_de/

RUN rasa train --domain openHPI_de/domain.yml --data data/openHPI_de --out /app/models/openHPI_de/

ENTRYPOINT ["rasa"]
