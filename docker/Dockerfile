FROM joyzoursky/python-chromedriver:3.9-selenium
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install --progress-bar off -r requirements.txt
COPY . /code/
