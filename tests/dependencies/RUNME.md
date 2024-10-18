# Command Dependencies

## clean # Clean build directory

```bash
rm -rf ./build
```

### format # Format the source code

```bash
npx prettier --write .
```

## build # Build the project

    - clean
    - format

```bash
npm run build
```

### deploy # Deploy to surge.sh

    build

```bash
surge ./build my-project.surge.sh
```

## no-description # hide

```bash
echo "no-description"
```
