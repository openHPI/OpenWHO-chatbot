FROM rasa/rasa:1.10.8-full

COPY config.yml /app/config.yml
COPY credentials.yml /app/credentials.yml
COPY endpoints.yml /app/endpoints.yml
COPY projects/openWHO/* /app/projects/openWHO/
COPY projects/GreetBot/* /app/projects/GreetBot/


RUN rasa train --out /app/models

ENTRYPOINT ["rasa"]