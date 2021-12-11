from setuptools import setup, find_packages


setup(
    name="insutance",
    version="0.0.2",
    description="Hey insutance! Who are you?",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="insutance",
    author_email="insutance@naver.com",
    url="https://github.com/insutance/hey-insutance",
    python_requires=">= 3.8",
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "hey = insutance.main:main"
        ]
    },
    package_data={},
    include_package_data=True
)
