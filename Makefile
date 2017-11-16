%.pdf: %.md
	pandoc -t beamer -V theme=metropolis -o $@ $<
