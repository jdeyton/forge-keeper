# stacks

## backend

This is the primary forge-keeper backend currently consisting of a database and
web server hosting the API.

### How to Deploy

- Ensure you have the database and web server Docker images built for the local
  swarm node. Refer to the `forge-tools/forge-psql` and
  `forge-keeper/src/data-server` projects for more details.
- Ensure you have all necessary docker secrets.
- Deploy the stack: `docker stack deploy -c backend.yml forge-keeper`

### How to Debug

Here are some helpful commands for debugging:

* `docker service ls` - Lists all docker services running.
* `docker service logs --follow --no-trunc SERVICE` - Shows the running
  log output of the specified service.
