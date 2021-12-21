# our base image
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 5000

COPY . .

RUN init.sh 

ENTRYPOINT ["./start.sh"]


# run the application
# CMD ["pipenv", "python", "main.py"]
