all:
	pdflatex main.tex 
	bibtex reference.aux
	pdflatex main.tex 
	pdflatex main.tex

clean:
	rm *.pdf *.aux *.log *.toc *.bbl