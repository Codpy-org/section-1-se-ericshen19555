# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11

COPY . .
# Install Flask
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8088",  "--reload"]