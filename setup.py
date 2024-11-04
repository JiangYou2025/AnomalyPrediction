from setuptools import setup, find_packages

setup(
    name="anomaly-prediction",                  # Package name (used for pip install)
    version="0.1.0",                            # Initial version
    description="A library for anomaly prediction in time series data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jiang YOU",
    author_email="jiang.you@esiee.fr",
    url="https://github.com/JiangYou2025/AnomalyPrediction",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[                          # List of dependencies
        "numpy",
        "pandas",
        "torch",
        "pickle",
        "matplotlib",
        "sklearn",
        # Add any other dependencies your library needs
    ],
    classifiers=[                               # Additional metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
