FROM python:3.8-slim AS base-test-env

WORKDIR /app

COPY . ./

RUN apt update && \
    apt install -y sqlite

RUN python3 -m ensurepip --default-pip && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.tests.txt

RUN mkdir base/

RUN python3 build_database.py

RUN pytest -v test_zipcode_app.py


FROM alpine AS production-env
# Necessary packages
RUN apk update && \
    apk add --no-cache py3-psutil python3 sqlite tzdata && \
    python3 -m ensurepip --default-pip && \
    pip install --no-cache-dir --upgrade pip

# Timezone America/Sao_Paulo
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime
RUN echo "America/Sao_Paulo" >/etc/timezone

# APP
WORKDIR /app

COPY main.py /app/
COPY sqlite_db.py /app/
COPY zipcode_*.py /app/
COPY requirements.txt /app/
COPY --from=base-test-env /app/base/cep.db /app/base/cep.db

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]