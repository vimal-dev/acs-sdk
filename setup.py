from setuptools import setup, find_packages

setup(
    name="acs_sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "httpx (>=0.28.1,<0.29.0)",
        "pydantic (>=2.12.5,<3.0.0)",
        "click (>=8.3.1,<9.0.0)",
        "opentelemetry-sdk (>=1.40.0,<2.0.0)",
    ],
    author="Vimal Kumar Saini",
    description="Python SDK for Apache CloudStack API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com",
)
