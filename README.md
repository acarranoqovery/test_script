22334445t3
# test_script

build:
docker build -t pythonimage .

run:
docker run --entrypoint="python" pythonimage "/home/main.py"
