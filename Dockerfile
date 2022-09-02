FROM python:3.7.6

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .

WORKDIR /usr/src/app

# CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]

ENTRYPOINT ["python"]
CMD ["app.py"]