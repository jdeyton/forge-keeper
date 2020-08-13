FROM python:3.8.5-slim-buster as base

COPY pip.conf pip.conf
ENV PIP_CONFIG_FILE pip.conf
RUN python3 -m pip install --no-cache-dir \
    digital-forge-drone
RUN rm pip.conf

FROM base as final
ENTRYPOINT ["py-drone"]