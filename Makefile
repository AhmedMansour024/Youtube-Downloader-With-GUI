# Define default task
.PHONY: all
all: install

# Create virtual environment
.PHONY: venv
venv:
	python -m venv venv
	
# Activate virtual environment
.PHONY: activate
activate:
	venv\Scripts\activate

# Install dependencies and upgrade pip using python -m pip
.PHONY: install
install: venv
	venv/Scripts/python -m pip install -r requirements.txt
	python.exe -m pip install --upgrade pip

# Clean up the environment
.PHONY: clean
clean:
	rm -rf venv
