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

## @build

Build the project

```sh
echo "Running default build target..."
npm run build
```

## @build: format compile docker-build

Build the project by running Node.js build and compiling Rust modules

```sh
echo "Building Node.js app..."
npm run build
```

## @clean

Clean build artifacts

```sh
echo "Cleaning build directory..."
rm -rf ${BUILD_DIR}
echo "Cleaning Rust modules..."
cargo clean --manifest-path ${RUST_MODULE_DIR}/Cargo.toml
echo "Done cleaning."
```

## @format

Format code for both Node.js and Rust

```sh
echo "Formatting Node.js files..."
npm run format
echo "Formatting Rust files..."
cargo fmt --manifest-path ${RUST_MODULE_DIR}/Cargo.toml
```

## @compile compile

Compile Rust modules

```sh
echo "Compiling Rust modules..."
cargo build --manifest-path ${RUST_MODULE_DIR}/Cargo.toml --release
```

## @docker-build

Build the Docker image for the app

```sh
echo "Building Docker image..."
docker build -t ${DOCKER_IMAGE} .
```

## @docker-run: docker-clean docker-build

Run the Docker image locally

```sh
echo "Running Docker image..."
docker run -p 3000:3000 ${DOCKER_IMAGE}
```

## Deploy commands for various environments

### @deploy-local: build

Deploy locally

```sh
echo "Deploying to local environment..."
docker-compose up --build
```

### @deploy-dev: build

Deploy to development

```sh
echo "Deploying to development environment..."
docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE}:dev
docker push ${DOCKER_IMAGE}:dev
echo "Deployed to development!"
```

### @deploy-staging: build

Deploy to staging

```sh
echo "Deploying to staging environment..."
docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE}:staging
docker push ${DOCKER_IMAGE}:staging
echo "Deployed to staging!"
```

### @deploy-prod: build

Deploy to production

```sh
echo "Deploying to production environment..."
docker tag ${DOCKER_IMAGE} ${DOCKER_IMAGE}:prod
docker push ${DOCKER_IMAGE}:prod
echo "Deployed to production!"
```

## @shell

Invoke shell example

```sh
echo "Running a custom shell command..."
bash -c "echo 'Hello from makedown shell invocation!'"
```
