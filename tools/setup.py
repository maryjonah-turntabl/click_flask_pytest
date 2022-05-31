from setuptools import setup

setup(
    name="weather-cli",
    version="1.0.0",
    py_modules=["weather_cli"],
    install_requires=[
        "Click",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'weather=weather_cli:weather',
        ]
    }
)