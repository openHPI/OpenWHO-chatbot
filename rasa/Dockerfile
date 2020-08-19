FROM rasa/rasa:1.10.8-full

COPY config.yml /app/projects/openWHO/config.yml
COPY credentials.yml /app/credentials.yml
COPY endpoints.yml /app/endpoints.yml
COPY projects/openWHO/* /app/projects/openWHO/

RUN rasa train --domain /app/projects/openWHO/domain.yml --data /app/projects/openWHO/data/ --out /app/models/openWHO

ENTRYPOINT ["rasa"]