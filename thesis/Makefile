all: clean build rename-to-hash

clean:
	./clean.sh

build: rasterize-pdfs
	lualatex thesis.tex
	bibtex thesis
	makeglossaries thesis
	lualatex thesis.tex
	lualatex thesis.tex
	lualatex thesis.tex

rasterize-pdfs:
	./rasterize-pdfs.sh

rename-to-hash: GIT_COMMIT=$(shell git rev-parse HEAD)
rename-to-hash:	
	mv thesis.pdf thesis_commit-$(GIT_COMMIT).pdf
