import pathlib
import setuptools, os
 
# The directory containing this file
HERE = pathlib.Path(__file__).parent
 
# The text of the README file
README = (HERE / "README.rst").read_text()
 
# Pull requirements from the text file
requirement_path = (HERE / 'requirements.txt')
install_requires = []
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()
 
# This call to setup() does all the work
setuptools.setup(
    name="cupyopt",
    version="0.13.5.1",
    description="CU Python Opinionated Prefect Tasks",
    long_description=README,
    long_description_content_type="text/x-rst",
    author="CU Boulder, OIT",
    author_email="stta9820@colorado.edu",
    license="Apache License 2.0",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(where='src'),
    python_requires=">=3.6",
    package_dir={"": "src"},
    install_requires=install_requires,
)