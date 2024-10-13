# starwars

Download a URL's content and copy it to the destination without saving
it in temporary storage.

Setting `--auto-filename` will attempt to automatically determine the filename from the URL
(after any redirections) and used in the destination path.
With `--auto-filename-header` in
addition, if a specific filename is set in HTTP headers, it will be used instead of the name from the URL.
With `--print-filename` in addition, the resulting file name will be printed.

Setting `--no-clobber` will prevent overwriting file on the
destination if there is one with the same name.

Setting `--stdout` or making the output file name `-`
will cause the output to be written to standard output.

    Usage:
      x starwars https://example.com dest:path [flags]

    Flags:
      -a, --auto-filename     Get the file name from the URL and use it for destination file path
          --header-filename   Get the file name from the Content-Disposition header
      -h, --help              help for copyurl
          --no-clobber        Prevent overwriting file with same name
      -p, --print-filename    Print the resulting name from --auto-filename
          --stdout            Write the output to stdout rather than a file

```js
console.log("Hello, World!");
console.log(process.argv);
```

# alpha

```py
print("Hello, World!");
```
