from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="your_package_name",
    version="1.0.0",
    author="your_author_name",
    description="Your short description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_author_name/your_package_name",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "genanki>=0.11.0",
        "Markdown>=3.3.4",
    ],
    package_data={
        "your_package_name": [
            "resource_file.txt",
        ],
    },
    entry_points={
        "console_scripts": [
            #"your_package_name_init=your_package_name:main_init",
            "your_package_name=your_package_name:main",
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/your_author_name/your_package_name/issues",
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
