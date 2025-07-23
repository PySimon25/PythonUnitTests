# .PHONY is a special target that declares certain targets as not representing real files. 
# This is useful for targets like "clean" or "install" which don't produce output files, or
# targets that should always be rebuilt regardless of whether a file of the same name exists
.PHONY: test

test:
	python -m unittest discover -s test
