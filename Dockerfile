FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /code
ADD Pipfile Pipfile.lock ./
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    apt update && apt install gcc g++ libgeos-dev && \
    python -m venv $VIRTUAL_ENV && \
    pip install --upgrade pip setuptools wheel && \
    pip install pipenv && \
    pipenv install --system --skip-lock && \
    useradd -ms /bin/bash dalvere && \
    chmod +x /code && chown dalvere:dalvere /code

ADD . /code
EXPOSE 8000
USER dalvere
ENTRYPOINT ["./entrypoint.sh"]
