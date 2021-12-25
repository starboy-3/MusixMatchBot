# our base image
FROM python:3.9

COPY . .

RUN sudo -H pip install --user pipenv
RUN pipenv install -r requirements.txt

ENTRYPOINT ["bash", "./start.sh"]


# run the application
# CMD ["pipenv", "python", "main.py"]
