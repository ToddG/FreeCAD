.PHONY: help
.SILENT: help
help:	## print help message
	@grep -Eh '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## build the entire app
	mkdir -p ../../../build
	rm -rf ../../../build/Mod/SearchBar
	(cd  ../../../build && cmake ../ && make -j$(nproc --ignore=2))

.PHONY: flake8
flake8: ## lint with flake8
	${run} flake8 .

.PHONY: isort
isort:	## lint with isort
	${run} isort .

.PHONY: black
black:	## lint with black
	${run} black .

.PHONY: lint
lint: isort black flake8 ## run linters [isort, black, flake8]