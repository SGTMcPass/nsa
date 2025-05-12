.PHONY: build run clean docker-run docker-clean compose-up compose-down test docker-visualize

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

compose-up:
	docker-compose up --build

compose-down:
	docker-compose down

test:
	python3 -m unittest discover tests/

docker-visualize:
	docker run --rm -v /home/rmcphail/repos/nasa-simulation-agents/rl/rl_project/output:/app/output rl_agent
