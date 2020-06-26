all: check-conda figures


check-conda:
	conda info | sed -rn 's@^\s*active environment : (.+)?\s*@\1@g p' | grep bachelors-thesis >/dev/null || ( echo 'Make you activate the Conda environment "bachelors-thesis" first ("conda activate bachelors-thesis")!'; exit 126 )


figures:
	python small-angle-approximation.py

