# Project settings

```sh
NODE_APP="my-node-app"
DOCKER_IMAGE="${NODE_APP}-image"
RUST_MODULE_DIR="rust_modules"
BUILD_DIR="build"
```

# Environment settings

```sh
PRODUCTION="production"
STAGING="staging"
DEVELOPMENT="development"
LOCAL="local"
```

# Command dependencies

```sh
# No direct analog for .PHONY in makedown, all commands are considered executable
```

## Default target: build the project

```sh build
echo "Running default build target..."
npm run build
```

## Build the project by running Node.js build and compiling Rust modules

```sh build: format compile docker-build
echo "Building Node.js app..."
npm run build
```

## Clean build artifacts

```sh clean
echo "Cleaning build directory..."
rm -rf ${BUILD_DIR}
echo "Cleaning Rust modules..."
cargo clean --manifest-path ${RUST_MODULE_DIR}/Cargo.toml
echo "Done cleaning."
```

## Format code for both Node.js and Rust

```sh format
echo "Formatting Node.js files..."
npm run format
echo "Formatting Rust files..."
cargo fmt --manifest-path ${RUST_MODULE_DIR}/Cargo.toml
```

## Compile Rust modules

```sh compile compile
echo "Compiling Rust modules..."
cargo build --manifest-path ${RUST_MODULE_DIR}/Cargo.toml --release
```

## Build the Docker image for the app

```sh docker-build
echo "Building Docker image..."
docker build -t ${DOCKER_IMAGE} .
```

## Run the Docker image locally

```sh docker-run: docker-clean docker-build
echo "Running Docker image..."
docker run -p 3000:3000 ${DOCKER_IMAGE}
```

## Deploy commands for various environments

### Deploy locally

```sh deploy-local: build
echo "Deploying to local environment..."
docker-compose up --build
```

### Deploy to development

```sh deploy-dev: build
echo "Deploying to development environment..."
docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE}:dev
docker push ${DOCKER_IMAGE}:dev
echo "Deployed to development!"
```

### Deploy to staging

```sh deploy-staging: build
echo "Deploying to staging environment..."
docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE}:staging
docker push ${DOCKER_IMAGE}:staging
echo "Deployed to staging!"
```

### Deploy to production

```sh deploy-prod build
echo "Deploying to production environment..."
docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE}:prod
docker push ${DOCKER_IMAGE}:prod
echo "Deployed to production!"
```

## Invoke shell example

```sh shell
echo "Running a custom shell command..."
bash -c "echo 'Hello from makedown shell invocation!'"
```
