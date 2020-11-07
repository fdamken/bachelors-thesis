all: clean build

clean:
	./clean.sh

build:
	lualatex thesis.tex
	bibtex thesis
	makeglossaries thesis
	lualates thesis.tex
	lualatex thesis.tex
	lualatex thesis.tex
