# Variable to determine the current environment
UNAME := $(shell uname)

# General install target
install:
ifeq ($(UNAME), Linux)
	@echo "Installing libraries on Linux"
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
	sudo apt-get install -y python3-tk
endif
ifeq ($(UNAME), Darwin)
	@echo "Installing libraries on macOS"
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt
	brew install python-tk
endif
ifeq ($(findstring MINGW, $(UNAME)), MINGW)
	@echo "Installing libraries on Windows"
	python -m venv venv
	venv\Scripts\activate && pip install -r requirements.txt
endif

# Target to run main.py
run:
ifeq ($(UNAME), Linux)
	source venv/bin/activate && python main.py
endif
ifeq ($(UNAME), Darwin)
	source venv/bin/activate && python main.py
endif
ifeq ($(findstring MINGW, $(UNAME)), MINGW)
	venv\Scripts\activate && python main.py
endif

# Clean target
clean:
	@echo "Cleaning up the virtual environment"
	rm -rf venv
