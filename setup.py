import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

install_requires = [
    "numpy",
    "matplotlib",
    "pillow",
    "qtpy",
    "termcolor",
    "imgviz",
    "PyYAML",
    "PyQt5",
]

setuptools.setup(
    name="labelpoints",  # Replace with your own username
    version="0.0.1",
    author="ScCcEe",
    author_email="scccwe@qq.com",
    description="a tool for only points",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/ScCcWe/labelpoints",
    packages=install_requires,
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
