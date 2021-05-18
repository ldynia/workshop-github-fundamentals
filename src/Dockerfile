FROM python:3.7.9-alpine

# Setup environment variables
ENV PORT=8080 \
    HOST=0.0.0.0 \
    FLASK_APP=/app/run.py \
    PYTHONUNBUFFERED=True
ARG FLASK_DEBUG=False
ENV FLASK_DEBUG=$FLASK_DEBUG

# Setup file system
WORKDIR /app
COPY app/ /app

# Upgrade pip & install python packages
RUN pip install --upgrade pip --requirement /app/requirements.txt

# Indicate which port to expose
EXPOSE $PORT

# Start app server
CMD flask run --host=$HOST --port=$PORT