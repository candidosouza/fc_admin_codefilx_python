FROM python:3.10.2

RUN apt update && apt install -y --no-install-recommends git curl wget \
    && python -m pip install --upgrade pip

RUN useradd -ms /bin/bash python && \
    chown -R python:python /var/log

RUN pip install pdm

USER python

WORKDIR /home/python/app

ENV MY_PYTHON_PACKAGES=/home/python/app/__pypackages__/3.10
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin

RUN echo 'eval "$(pdm --pep582)"' >> ~/.bashrc

CMD ["tail", "-f", "/dev/null"]