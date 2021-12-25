FROM ubuntu:20.04
COPY . .

RUN apt-get update

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
