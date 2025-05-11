.PHONY: build run clean docker-run docker-clean

build:
	docker build -t rl_agent:latest .

run:
	python3 main.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

docker-run:
	docker run --rm rl_agent

docker-clean:
	docker container prune -f
	docker image prune -a -f
