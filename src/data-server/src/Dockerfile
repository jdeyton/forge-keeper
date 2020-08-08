FROM python:3.8.5-slim-buster as base

ARG ARCH
RUN if [ "$ARCH" = "armhf" ]; then apt update && apt install -y gcc libpq-dev; fi

COPY pip.conf pip.conf
ENV PIP_CONFIG_FILE pip.conf
RUN python3 -m pip install --no-cache-dir \
    digital-forge-data-server
RUN rm pip.conf

FROM base as final
EXPOSE 50080
ENTRYPOINT ["python3", "-m", "digital.forge.data.server"]
