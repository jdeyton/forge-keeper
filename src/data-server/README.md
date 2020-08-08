# forge-data-server

## How to Build

- Generate code: `make .codegen`
  * If you are *regenerating* code, the controllers will be replaced. It may be
    desired to revert changes to them.
  * Tests should generally not be re-generated. Subsequent attempts will fail
    because the OpenAPI utility tries to bury them in the `src` tree.
- Make the distributable Python files: `make dist`
- Ensure the local/temporary PyPI server is running.
- Copy the appropriate `pip.conf` for read access to the PyPI server into
  `./context`.
- Build the Docker image:
  * If on a typical system architecture: `make forge-data-server-docker.tgz`
  * If on an `armhf` architecture: `docker build --build-arg ARCH=armhf --network host -t forge-data-server context`

## How to Deploy

After ensuring the necessary secrets are in place:

```
docker stack deploy -c stack.yml forge-keeper
```