# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN export PYTHONPATH="$PYTHONPATH:/app"
ENTRYPOINT ["python"]
CMD ["app.py"]