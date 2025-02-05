### **5. Build & Install the SDK**
Run the following commands to package and install:

```sh
# Create a source distribution
python setup.py sdist

# Install the package locally
pip install .


If you want to distribute your SDK via PyPI:

sh
Copy
Edit
pip install twine
python setup.py sdist
twine upload dist/*
This makes it available for installation via:

sh
Copy
Edit
pip install my_sdk