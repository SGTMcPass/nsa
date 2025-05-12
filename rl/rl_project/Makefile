.PHONY: clean spotless docker-build docker-run docker-clean docker-rebuild

# === Docker Commands ===
docker-build:
	@echo "🐳 Building Docker image 'rl_agent:latest'..."
	@docker build -t rl_agent:latest .

docker-run:
	@echo "🐳 Running Docker container for RL Agent..."
	@docker run -it --rm \
		--user $(USER_ID):$(GROUP_ID) \
		-v $(PWD)/output:/app/output rl_agent
docker-clean:
	@echo "🗑️  Cleaning up Docker containers and images..."
	-@docker stop $$(docker ps -aq --filter ancestor=rl_agent) 2>/dev/null || true
	-@docker rm $$(docker ps -aq --filter ancestor=rl_agent) 2>/dev/null || true
	-@docker rmi rl_agent:latest --force 2>/dev/null || true
	-@docker image prune -f

docker-rebuild: docker-clean docker-build
	@echo "🔄 Docker image rebuilt successfully!"

# === Local Cleanup ===
clean:
	@echo "🗑️  Removing local output files..."
	rm -rf output/*.png
	rm -rf output/*.gif
	rm -rf output/*.log
	rm -rf output/*.pkl
	@echo "✅ Local cleanup complete."

# === Spotless Cleanup (Docker + Local) ===
spotless: clean docker-clean
	@echo "🚀 All Docker containers, images, and generated files have been removed!"
