FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
RUN groupadd -r deepuser && useradd -r -g deepuser deepuser
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8009
RUN chmod +x entry.sh
ENTRYPOINT ["/app/entry.sh"]
