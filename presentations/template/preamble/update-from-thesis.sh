#!/bin/bash

cp ../../../thesis/preamble/packages.tex .
# Remove the theorem definitions as beamer already defines them.
sed -r 's@^\\newtheorem\{(theorem|definition|lemma)\}.+$@@g' ../../../thesis/preamble/styles.tex >styles.tex
