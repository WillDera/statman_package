import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='statman',
                 version='0.1.1',
                 author="Chinenye Raphael, Ezeoke Godswill",
                 author_email="cudraphael@gmail.com",
                 description='Statistical Distribution',
                 long_description_content_type="text/markdown",
                 url="https://github.com/Rapixar/statman_package",
                 packages=setuptools.find_packages(),
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.6',
                 )
