all: clean rasterize-pdfs build rename-to-hash

clean:
	./clean.sh

build:
	lualatex thesis.tex
	bibtex thesis
	makeglossaries thesis
	lualatex thesis.tex
	lualatex thesis.tex
	lualatex thesis.tex

rasterize-pdfs:
	find . -type f -name '*.pdf' -print0 | while IFS= read -r -d '' file; do pdftoppm -singlefile -png "$file" "$(sed 's/.pdf$//' <<<"$file")"; done

rename-to-hash: GIT_COMMIT=$(shell git rev-parse HEAD)
rename-to-hash:	
	mv thesis.pdf thesis_commit-$(GIT_COMMIT).pdf
