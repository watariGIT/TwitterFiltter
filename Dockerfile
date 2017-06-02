FROM python:2.7-onbuild
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","./Tweet.py"]