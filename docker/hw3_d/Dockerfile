FROM python:latest
WORKDIR /app
COPY requirements.txt memory_info.py ./
RUN pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
VOLUME /data
ENTRYPOINT ["python3", "memory_info.py"]