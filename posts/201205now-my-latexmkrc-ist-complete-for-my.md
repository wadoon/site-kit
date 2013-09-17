<!--
.. title: latexmk workflow
.. date: 2012/05/21 16:05:00
.. slug:
-->

Now my latexmkrc ist complete for my thesis I post it. 
It is adopted to my workflow and uses Incskape, Graphviz for figure creation and works with *nomencl* package.


    
	# $HOME/.latexmkrc 
	$pdf_previewer = "start evince";
	$pdf_update_method = 0;

	add_cus_dep( "svg", "pdf", 1, 'svg2pdf');
	add_cus_dep( "dot", "pdf", 1, 'dot2pdf');
	add_cus_dep( "nlo", "nls", 1, 'nomencl');


	sub svg2pdf {
	    system("inkscape  $_[0].svg -A $_[0].pdf --export-area-drawing --export-dpi=600");
	}

	sub dot2pdf {
	    system("dot -Tpdf -o $_[0].pdf   $_[0].dot");
	}

	sub nomencl {
	    system("makeindex $_[0].nlo -s nomencl.ist -o $_[0].nls");
	}


