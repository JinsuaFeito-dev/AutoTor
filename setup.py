import setuptools
import os.path

source = "src"
pkg = "autotor"

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    required = f.read().splitlines()

metadata = {}
with open(os.path.join(source, pkg, "_metadata.py")) as f:
     exec(f.read(), metadata)

    
setuptools.setup(
    name = metadata["__name_pkg__"],
    version = metadata["__version__"],
    description = metadata["__description__"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = metadata["__url__"],
    python_requires = metadata["__python_requires__"],
    install_requires = required,
    package_dir = {"": source},
    packages = setuptools.find_packages(where = source),
    classifiers = metadata["__classifiers__"]
)