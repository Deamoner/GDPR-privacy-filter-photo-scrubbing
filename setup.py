from setuptools import find_packages, setup

with open("README.md", "r") as f:
    DESCRIPTION = f.read()

setup(
    name="privy-filter",
    version="0.1.0",
    description="Privacy Photo filter for GDPR compliant photo sharing and machine learning without bias.",
    url="https://github.com/deamoner/privy-filter",
    author="Mattthew Davis AKa Deamoner",
    author_email="mdavis@virtustructure.com",
    license="MIT",
    packages=["privy-filter"],
    keywords="photo privacy de-identification anonymization",
    install_requires=["numpy>=1.18.4",
    "opencv-python>=4.2.0.34",
    "matplotlib"]
)
classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Topic :: Software Development",
          "Topic :: Photo Privacy :: Indexing",
          "Topic :: Utilities"
      ]
