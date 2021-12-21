# our base image
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 5000

COPY . .

RUN pip install pipenv
RUN pipenv install -r requirements.txt

ENTRYPOINT ["./start.sh"]


# run the application
# CMD ["pipenv", "python", "main.py"]
