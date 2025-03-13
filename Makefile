# Define variables
DOCKER_IMAGE=gesture_control
CONTAINER_NAME=gesture-container

# Install the dependancies
deps:
	pip3 install -r requirements.txt

# Run the project locally
run-local:
	python3 main.py

# Build and run the project in Docker
build:
	docker build -t $(DOCKER_IMAGE):latest .

run-docker:
	docker run --rm -it --env HUE_BRIDGE_IP=$(HUE_BRIDGE_IP) --device /dev/video0:/dev/video0 --name $(CONTAINER_NAME) $(DOCKER_IMAGE)

# Run using Docker Compose
up:
	docker-compose up --build -d

down:
	docker-compose down

# Remove all stopped containers and dangling images
clean:
	docker system prune -f

# Stop and remove the container manually
stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)