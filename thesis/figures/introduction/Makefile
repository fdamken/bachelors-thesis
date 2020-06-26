all: check-conda clean figures


check-conda:
	conda info | sed -rn 's@^\s*active environment : (.+)?\s*@\1@g p' | grep bachelors-thesis >/dev/null || ( echo 'Make you activate the Conda environment "bachelors-thesis" first ("conda activate bachelors-thesis")!'; exit 126 )


clean:
	rm -rf generated


figures:
	mkdir -p generated
	python pendulum-motion.py
	python small-angle-approximation.py

