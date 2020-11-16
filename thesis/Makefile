all: clean build

clean:
	./clean.sh

build:
	lualatex thesis.tex
	bibtex thesis
	makeglossaries thesis
	lualatex thesis.tex
	lualatex thesis.tex
	lualatex thesis.tex
	mv thesis.pdf thesis_commit-$(git rev-parse HEAD).pdf
