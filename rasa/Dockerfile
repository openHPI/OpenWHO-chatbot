FROM rasa/rasa:latest-full

COPY config.yml /app/config.yml
COPY openWHO/domain.yml /app/openWHO/domain.yml
COPY credentials.yml /app/credentials.yml
COPY endpoints.yml /app/endpoints.yml
COPY data/openWHO/* /app/data/openWHO/

RUN rasa train --domain openWHO/domain.yml --data data/openWHO --out /app/models/openWHO/

ENTRYPOINT ["rasa"]
