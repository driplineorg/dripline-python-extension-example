from setuptools import setup, find_namespace_packages

def set_version_data():
    import subprocess
    import re
    version_data = {}
    pwd = subprocess.check_output(['pwd'])
    print("pwd: {}".format(pwd))
    origin = subprocess.check_output(['git', 'remote', 'get-url', 'origin'])
    print("raw origin: '{}'".format(origin))

packages = find_namespace_packages('.', include=['dripline.extensions.*'])
print('packages are: {}'.format(packages))

setup(
    name="kv_plugin",
    setup_requires=['setuptools_scm'],
    use_scm_version={
        "root": ".",
        "write_to": "./version.py",
        'version_scheme': lambda x: "v{}".format(x.tag),
        'local_scheme': lambda x: "",
    },
    packages=packages,
)
