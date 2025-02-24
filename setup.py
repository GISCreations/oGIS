from setuptools import setup, find_packages

setup(
    name="Test_Project_oGIS",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points="""
        [console_scripts]
        your_command=your_package.module:main
    """,
)
