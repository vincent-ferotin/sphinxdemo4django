# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR      = src
BUILDDIR       = .
OUTPUTS        = doctrees \
  html
OUTPUT_DIRS    = $(foreach output,$(OUTPUTS),$(BUILDDIR)/$(output))

# Put it first so that "make" without argument is like "make help".
help:
	@echo "Please use `make target' where target is one of:"
	@echo "  html        to make standalone HTML files"
	@echo "  clean       to remove everything in the build directory"

.PHONY: \
  help \
  clean \
  html \
  Makefile

clean: Makefile
	@for dirname in $(OUTPUT_DIRS); do \
	    rm -Rf "$$dirname"; \
	done; unset dirname

html: Makefile
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
