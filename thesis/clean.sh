#!/bin/zsh

clean() {
	rm -f **/*.acn
	rm -f **/*.acr
	rm -f **/*.alg
	rm -f **/*.aux
	rm -f **/*.bbl
	rm -f **/*.blg
	rm -f **/*.lof
	rm -f **/*.log
	rm -f **/*.lot
	rm -f **/*.opg
	rm -f **/*.opi
	rm -f **/*.opo
	rm -f **/*.out
	rm -f **/*.syg
	rm -f **/*.synctex*
	rm -f **/*.syo
	rm -f **/*.sys
	rm -f **/*.toc
	rm -f **/*.xdy
	rm -f **/*.xmpdata
	rm -f **/pdfa.xmpi
	rm -f figures/**/*.png
	rm -f drawroom.pdf
	rm -f thesis.pdf
	touch thesis_commit-.pdf
	rm -f thesis_commit-*.pdf
}

clean &>/dev/null
