import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="labelpoints",  # Replace with your own username
    version="0.0.1",
    author="ScCcEe",
    author_email="scccwe@qq.com",
    description="a simply tool for points",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/ScCcWe/labelpoints",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.7',
    entry_points={
                "console_scripts": [
                    "labelme=labelme.__main__:main",
                ],
    },
)
