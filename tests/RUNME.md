# [clean]() Clean build directory

```bash
rm -rf ./build
```

# [format]() Format the source code

```bash
npx prettier --write .
```

# [build](clean format) Build the project

```bash
npm run build
```

## ![deploy](build one two three) Deploy to surge.sh

```bash
surge ./build my-project.surge.sh
```

## ![deploy](build,one,two,three) Deploy to surge.sh

```bash
surge ./build my-project.surge.sh
```

## [deploy](build,one,two,three) Deploy to surge.sh

```bash
surge ./build my-project.surge.sh
```
