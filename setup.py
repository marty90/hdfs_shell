try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="hdfs_shell",
    description="A simple HDFS shell.",
    license="GNU GENERAL PUBLIC LICENSE v3",
    version="1.0.0",
    author="Martino Trevisan",
    author_email="martino.trevisan@polito.it",
    maintainer="Martino Trevisan",
    maintainer_email="martino.trevisan@polito.it",
    url="https://github.com/marty90/hdfs_shell",
    packages=['hdfs_shell'],
    install_requires=[],
    scripts=['hdfs_shell/hdfs_shell']
)

# Upload on pip with:
# python setup.py sdist
# twine upload dist/*

# Install locally with:
# sudo python3 setup.py install
