from setuptools import setup

setup(
    name="flake8_stripe",
    version="0.1.0",
    py_modules=["flake8_stripe"],
    install_requires=[
        "flake8>=3.0.0",
    ],
    entry_points={
        "flake8.extension": [
            "SPY = flake8_stripe:TypingImportsChecker",
        ],
    },
)
