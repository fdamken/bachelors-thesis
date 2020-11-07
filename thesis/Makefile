all: clean build

clean:
	rm -f **/*.acn **/*.acr **/*.alg **/*.aux **/*.bbl **/*.blg **/*.lof **/*.log **/*.lot **/*.opg **/*.opi **/*.opo **/*.out **/*.syg **/*.synctex* **/*.syo **/*.sys **/*.toc **/*.xdy **/*.xmpdata drawroom.pdf **/pdfa.xmpi thesis.pdf

build:
	lualatex thesis.tex
	bibtex thesis
	makeglossaries thesis
	lualates thesis.tex
	lualatex thesis.tex
	lualatex thesis.tex
