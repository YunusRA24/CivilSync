FROM python:3.9-slim

EXPOSE 8501

RUN apt-get update && apt-get install -y build-essential software-properties-common git ssh \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install streamlit pandas altair plotly

ENTRYPOINT [ "streamlit", "run", "CivilSync.py", "--server.port=8501", "--server.address=0.0.0.0"]