FROM python:3.7
RUN pip install fastapi uvicorn
EXPOSE 80
COPY ./ /app/
RUN ls -la /app/*

RUN pip install -r /app/BlogImageProcessor/requirements.txt

WORKDIR "/app"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
