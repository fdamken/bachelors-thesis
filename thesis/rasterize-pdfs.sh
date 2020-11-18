#!/bin/bash

cd figures
find . -type f -name '*.pdf' -print0 | while IFS= read -r -d '' file; do
	echo "Rasterizing $file"
	pdftoppm -singlefile -png "$file" "$(sed 's/.pdf$//' <<<"$file")";
done
