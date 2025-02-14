FROM python:3.12-bullseye

WORKDIR /app
RUN useradd python

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY --chown=python:python src /app

RUN chown -R python:python /app
USER python

COPY . .

EXPOSE 8080
CMD ["python", "main.py"]