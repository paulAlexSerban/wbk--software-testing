setup_venv:
	@echo "Setting up virtual environment..."
	@python3.12 -m venv .venv

# run this manually if you want to activate the virtual environment - make does not support activating venvs directly
# activate_venv:
# 	@echo "Activating virtual environment..."
# 	. .venv/bin/activate

freeze_deps:
	@echo "Freezing dependencies..."
	@pip freeze > requirements.lock.txt
	@echo "Dependencies frozen."

install_deps:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt	
	@echo "Dependencies installed."

test:
	@echo "Running tests..."
	@pytest -v -s ./tests
	@echo "Tests completed."