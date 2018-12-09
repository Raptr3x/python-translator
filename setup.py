import setuptools

setuptools.setup(
    name="ptranslator",
    version="1.5.1",
    author="Bogdan Caleta Ivkovic",
    author_email="bogdan.caleta@gmail.com",
    description="Simple yet effective module for translating that uses Google Translate",
    url="https://github.com/Raptr3x/python-translator",
    packages=["ptranslator"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
          'console_scripts': [
              'ptranslator = ptranslator.ptranslator:main'
          ]
      },
)