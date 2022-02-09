FROM python:3.9

# Dependencies
COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry install

# Copy in app code
WORKDIR /service

COPY ..

# Ports etc
EXPOSE 3000

# Use the poetry venv to run the api
ENTRYPOINT ["poetry", "run", "python3", "-m" , "indexer.py", "start"]