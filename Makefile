dynamic-documents.pdf: dynamic-documents.md
	pandoc -t beamer -V theme=metropolis -o $@ $<
evergreen.%: evergreen.Rmd
	Rscript -e 'rmarkdown::render("$<", output_file = "$@")'
