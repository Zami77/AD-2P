pip install -r requirementsWebServer.txt
gunicorn AD2PApi:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80