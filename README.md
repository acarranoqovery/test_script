TT22334445t32
# test_script

build:
docker build -t pythonimage .

run:
docker run --entrypoint="python" pythonimage "/home/main.py"
