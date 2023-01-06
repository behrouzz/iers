from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="iers",
    version="0.0.1",
    author="Behrouz Safari",
    author_email="behrouz.safari@gmail.com",
    description="Analysis data of the International Earth Rotation Srvice (IERS)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/behrouzz/iers",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = find_packages(),
    include_package_data=True,
    install_requires=["numpy", "pandas"],
    python_requires='>=3.6',
)
