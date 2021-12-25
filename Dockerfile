FROM ubuntu:latest
COPY . .

RUN apt-get update

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow
RUN apt-get install -y tzdata

RUN apt-get install -y  \
            python3.9     \
            pip

RUN pip install -r requirements.txt

ENV BOT_TOKEN=${BOT_TOKEN}
ENV MUSIXMATCH_API_KEY=${MUSIXMATCH_API_KEY}

ENTRYPOINT ["python3", "main.py"]
CMD ["bash"]

# run the application
# CMD ["pipenv", "run", "python", "main.py"]
