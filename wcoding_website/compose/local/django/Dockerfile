FROM python:3.5

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

# -i: option is changing the word and saving the result specified file instead of output.
COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/local/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh

#COPY ./compose/local/django/celery/worker/start.sh /start-celeryworker.sh
#RUN sed -i 's/\r//' /start-celeryworker.sh
#RUN chmod +x /start-celeryworker.sh

#COPY ./compose/local/django/celery/beat/start.sh /start-celerybeat.sh
#RUN sed -i 's/\r//' /start-celerybeat.sh
#RUN chmod +x /start-celerybeat.sh

WORKDIR /app

# when a container is starting, excuting a script or a command.
# 'ENTRYPOINT' can be used only once in Dockerfile
ENTRYPOINT ["/entrypoint.sh"]
