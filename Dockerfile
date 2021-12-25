# our base image
FROM python:3.9

# specify the port number the container should expose
EXPOSE 5000

COPY . .

RUN sudo -H pip install --user pipenv
RUN pipenv install -r requirements.txt

ENTRYPOINT ["bash", "./start.sh"]


# run the application
# CMD ["pipenv", "python", "main.py"]
