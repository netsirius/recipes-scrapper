import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recipes-scrapper", # Replace with your own username
    version="1.0.0",
    author="Hector Santos",
    description="A recipes scrapper",
    packages=setuptools.find_packages('src', include=['nooddle_scrapper*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'beautifulsoup4==4.9.1',
        'selenium==3.141.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
         'pytest',
    ],
    test_suite='pytest',
    python_requires='>=3.6',
)