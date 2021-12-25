# our base image
FROM python:3.9

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["bash", "./start.sh"]


# run the application
# CMD ["pipenv", "python", "main.py"]
