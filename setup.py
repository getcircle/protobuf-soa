from setuptools import (
    find_packages,
    setup,
)

import service_protobufs

requirements = [
# TODO package requirements
]

setup_requirements = [
    'nose>=1.0',
    'coverage>=1.0',
    'mock==1.0.1',
]

setup(
    name='protobuf-soa',
    version=service_protobufs.__version__,
    description='service protobufs',
    packages=find_packages(exclude=[
        "*.tests",
        "*.tests.*",
        "tests.*",
        "tests",
    ]),
    install_requires=requirements,
    setup_requires=setup_requirements,
)
