This repo is an example of extending the dripline namespace with an extension python package.

It serves several purposes:
1. It leverages travis-ci to test that code changes don't break our ability to add extension modules.
2. It is (will be) the example used in the documentation for writing extensions
3. It includes working examples of the various boilerplate required.

## Quick start
- Run the dripline-python container, with the repo mounted in a known path.
- Build this plugin with `pip install <path/to/the/mount/point>`
- Run the example config with `dl-serve -c /path/to/the/mount/point/kv_store_tutorial.yaml` (you probably also need `--auth-file /some/path/to/auths.json`) in a known path.
