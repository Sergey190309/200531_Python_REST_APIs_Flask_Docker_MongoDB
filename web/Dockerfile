FROM python:3.8.3-slim-buster

# The below is convention
WORKDIR /usr/src/app

# The file with python packages should be installed.
COPY requirements.txt .
# nstall packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project to working directory.
COPY . .

CMD [ "python", "app.py" ]
