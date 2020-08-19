FROM rasa/rasa:1.10.8-full

COPY config.yml /app/config.yml
COPY credentials.yml /app/credentials.yml
COPY endpoints.yml /app/endpoints.yml
COPY data/* /app/data/
COPY domain.yml /app/domain.yml

RUN rasa train --out /app/models/openWHO/

ENTRYPOINT ["rasa"]