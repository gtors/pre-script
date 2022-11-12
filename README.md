# Pre Script

Util for executing a custom script before running any python application or script without modifying the last one.

You may treat it as application pre-start hook.

## Use cases
- patching log configs for a legacy application (sometimes it's pretty hard)
- auto-executing `docker-compose.yml` before running the application
- patching the application module (sometimes usefull for debugging)
- any case where you need to inject some temporary logic without modifying the application code base

## Installation

```console
$ pip install pre-script
```

## Example

```console
$ echo PRE_SCRIPT_ENABLED=1
$ echo 'print("hello from pre-script")' > .pre-script.py
$ echo 'print("hello from app")' > app.py
```

```console
$ python app.py
$ hello from pre-script
$ hello from app
```

If required, the script name can be changed via `PRE_SCRIPT_FILE` environment variable.

## License

Distributed under the terms of the [MIT license][license],
_Pre Script_ is free and open source software.
