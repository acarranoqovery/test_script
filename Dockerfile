FROM python:3.8-slim-buster
ADD job.py job.py
ADD cronjob.py cronjob.py
CMD ["python", "cronjob.py"]
ENTRYPOINT ["/bin/bash -c"]
