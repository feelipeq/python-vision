settings=src.settings.base

ifdef SIMPLE_SETTINGS
	settings=$(SIMPLE_SETTINGS)
else
	export SIMPLE_SETTINGS=$(settings)
endif

export PYTHONPATH=$(shell pwd)/src
export GOOGLE_APPLICATION_CREDENTIALS=$(PYTHONPATH)/secrets/Quickstart-09f65f8f8289.json