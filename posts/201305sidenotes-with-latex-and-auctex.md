<!--
	.. title: Sidenotes with LateX and Auctex
	.. slug:
	.. date: 2013/05/01
-->

I often use the following Latex snippet for creating small notes (like
paragraphs headings) for the reader's orientation: 

    \newcommand\sidenote[1]{\marginpar{{\small \textsf{\textbf{#1}}}}}

This creates in the margin a smaller bolder sans-serif heading. If you want to
hide this macro within the fold-mode of auctex, you need to adapt following list
(see here):



__**User Option:**__ **TeX-fold-macro-spec-list**
<blockquote>
List of replacement specifiers and macros to fold. The
specifier can be a string, an integer or a function symbol. If you specify a
string, it will be used as a display replacement for the whole macro. Numbers in
braces, brackets, parens or angle brackets will be replaced by the respective
macro argument. For example ‘{1}’ will be replaced by the first mandatory
argument of the macro. One can also define alternatives within the specifier
which are used if an argument is not found. Alternatives are separated by ‘||’.
They are most useful with optional arguments. As an example, the default
specifier for ‘\item’ is ‘[1]:||*’ which means that if there is an optional
argument, its value is shown followed by a colon. If there is no optional
argument, only an asterisk is used as the display string. If you specify a
number as the first element, the content of the respective mandatory argument of
a LaTeX macro will be used as the placeholder. If the first element is a
function symbol, the function will be called with all mandatory arguments of the
macro and the result of the function call will be used as a replacement for the
macro. The placeholder is made by copying the text from the buffer together with
its properties, i.e. its face as well. If fontification has not happened when
this is done (e.g. because of lazy font locking) the intended fontification will
not show up. As a workaround you can leave Emacs idle a few seconds and wait for
stealth font locking to finish before you fold the buffer. Or you just re-fold
the buffer with TeX-fold-buffer when you notice a wrong fontification.
</blockquote>

In our case we can need only to execute this:

    :::scheme
    (add-to-list 'TeX-fold-macro-spec-list
		'("[sidenote]" ("sidenote")))

From the documentation you can derive this:

	:::bnf
    TeX-fold-macro-spec-list :=	( specifier* )
	specifier                := ( {integer, symbol, string}  list-of-tex-macros)
	list-of-tex-macros       := ( string* )

If we pass a string, the macro (+ arguments) will be replaced in fold by this
string. If we use “{n}” (or brackets, parens or angle brackets) the macro will
be substitue by the n-th argument. The same as you use an integer value. An
symbol with a bound function will be called by the macro mandatory arguments.


Inspect *TeX-fold-macro-spec-list* for more details:

	:::scheme
    (("[f]"     ("sidenote"))
	 ("[f]"     ("footnote" "marginpar"))
	 ("[c]"     ("cite"))
	 ("[l]"     ("label"))
	 ("[r]"     ("ref" "pageref" "eqref"))
	 ("[i]"     ("index" "glossary"))
	 ("[1]:||"  ("item"))
	 ("…"       ("dots"))
	 ("(C)"     ("copyright"))
	 ("(R)"     ("textregistered"))
	 ("TM"      ("texttrademark"))
	 (1         ("part" "chapter" "section" "subsection" "subsubsection"
	             "paragraph" "subparagraph" "part" "chapter" "section"
				 "subsection" "subsubsection" "paragraph" "subparagraph"
				 "emph" "textit" "textsl" "textmd" "textrm" "textsf"
				 "texttt" "textbf" "textsc" "textup")))
