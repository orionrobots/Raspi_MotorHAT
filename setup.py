import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Raspi_MotorHAT",
    version="0.0.2",
    author="Unknown author",
    author_email="Unknown",
    description="Code to interface with the Raspi_MotorHAT board.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/orionrobots/Raspi_MotorHAT",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Raspbian",
    ),
)
