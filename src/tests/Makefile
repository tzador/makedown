# Project settings
NODE_APP := my-node-app
DOCKER_IMAGE := $(NODE_APP)-image
RUST_MODULE_DIR := rust_modules
BUILD_DIR := build

# Environment settings
PRODUCTION := production
STAGING := staging
DEVELOPMENT := development
LOCAL := local

# Command dependencies
.PHONY: all build clean format compile docker-build docker-run deploy-local deploy-dev deploy-staging deploy-prod

# Default target: build the project
all: build

# Build the project by running Node.js build and compiling Rust modules
build: format compile docker-build
	@echo "Building Node.js app..."
	npm run build

# Clean build artifacts
clean:
	@echo "Cleaning build directory..."
	rm -rf $(BUILD_DIR)
	@echo "Cleaning Rust modules..."
	cargo clean --manifest-path $(RUST_MODULE_DIR)/Cargo.toml
	@echo "Done cleaning."

# Format code for both Node.js and Rust
format:
	@echo "Formatting Node.js files..."
	npm run format
	@echo "Formatting Rust files..."
	cargo fmt --manifest-path $(RUST_MODULE_DIR)/Cargo.toml

# Compile Rust modules
compile:
	@echo "Compiling Rust modules..."
	cargo build --manifest-path $(RUST_MODULE_DIR)/Cargo.toml --release

# Build the Docker image for the app
docker-build:
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE) .

# Run the Docker image locally
docker-run:
	@echo "Running Docker image..."
	docker run -p 3000:3000 $(DOCKER_IMAGE)

# Deploy commands for various environments
deploy: deploy-local deploy-dev deploy-staging deploy-prod

deploy-local: build
	@echo "Deploying to local environment..."
	# Command to deploy locally (e.g., Docker compose)
	docker-compose up --build

deploy-dev: build
	@echo "Deploying to development environment..."
	# Command to deploy to development (e.g., Docker push, kubectl, etc.)
	docker tag $(DOCKER_IMAGE) $(DOCKER_IMAGE):dev
	docker push $(DOCKER_IMAGE):dev
	# Simulating deployment with a simple message
	@echo "Deployed to development!"

deploy-staging: build
	@echo "Deploying to staging environment..."
	# Command to deploy to staging (e.g., Docker push, kubectl, etc.)
	docker tag $(DOCKER_IMAGE) $(DOCKER_IMAGE):staging
	docker push $(DOCKER_IMAGE):staging
	@echo "Deployed to staging!"

deploy-prod: build
	@echo "Deploying to production environment..."
	# Command to deploy to production (e.g., Docker push, kubectl, etc.)
	docker tag $(DOCKER_IMAGE) $(DOCKER_IMAGE):prod
	docker push $(DOCKER_IMAGE):prod
	@echo "Deployed to production!"

# Example shell invocation for running specific commands
invoke-shell:
	@echo "Running a custom shell command..."
	@bash -c "echo 'Hello from Makefile shell invocation!'"
