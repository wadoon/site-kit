<!--
	.. title: Formale Spezifikation mit TLA<sup>+</sup>
	.. author: Alexander Weigl
	.. date: 2012-01-19	
-->

## Abstract

> TLA (Temporal Logic for Action) ist ein Sprache zum Beschreiben von
> System unter Verwendung von der Prädikatenlogik und  Linearer
> Temporalen Logik (LTL).
> LTL erweitert die Prädikatenlogik (propositional logic) um
> Aspekte einer diskreten zeitlichen Abfolge von aufeinander folgenden
> Zuständen. Mit der LTL werden Anfordungen über Liveness und Fairness
> an Systemen gestellt. Diese Arbeit erklärt die Syntax und Semantik
> von TLA anhand von Beispielen, sowie das spezifizieren von
> Fairness-Anforderungen in TLA-Spezifikationen.
> Der Abschluss der Arbeit stellt die Vorstellung des 
> Model-Checkers dar.


> TLA (Temporal Logic for Action) is a language for specifying systems
> with usage of propositional (PL) and linear temporal logic (LTL). LTL
> extends the propositional logic by quantors for statements about a
> linear discrete sequences about states. I explain liveness and
> fairness requirements in LTL. This paper shows the syntax and semantic
> of TLA with examples and point out the strong and week fairness
> properties in TLA. I conclude with an introduction of the
> modelchecker TLC within the TLA-Toolbox.	

## Bibtex

    @Unpublished = {
	  author={Alexander Weigl},
      title={Formale Spezifikation mit TLA\textsuperscript{+}},
      year=2011
    }


## Dateien


1. [Abstrakt/Thesenpapier (Version 1)](abstract_1.pdf)
   > Erläuterung der Gliederung, Darlegung des Arbeitsthema und Quellen
2. [Fragenkatalog (Version 1) mit Antworten](questions_1-answers-1.pdf)
    * [Fragenkatalog (Version 2) mit Antworten](questions_2-answers-2.pdf)   
	   > Fragen, die während der Einarbeitung gekommen 
	   > sind mit Anworten vom Prof. Rock.
3. <del>[Präsentation (Version 1)](presentation_1.pdf)</del>
4. [Präsentation (Version 2)](presentation_2.pdf)
5. [Publikation (Version 2)](publication_2.pdf) <del>[(Version 1)](publication_1.pdf)</del>


## Beispiele/Spezifikationen

* <a href="DieHard.tla">DieHard.tla</a>
  > Rätsel aus Stirb Langsam 3. Bestandteil aus den Beispielen von TLA

* <a href="DieHarder.tla">DieHarder.tla</a>
  >	  Erweiterung des Rätsel aus Stirb Langsam 3. 
  >	  Nun mit mehreren Krügen und versch. zu erreichenden Füllmengen.

* <a href="HourClock.tla">HourClock.tla</a>
  >  Klassisches Einführungsbeispiel einer Uhr.


* <a href="TrafficLight.tla">TrafficLight.tla</a>
  >  Beispiel einer Verkehrsampel mit drei Lampen (vier Zuständen)

* <a href="Euclid.tla">Euclid.tla</a>
  >  Euclidischer Algorithmus als Beispiel zu PlusCal

* <a href="FastMutex.tla">FastMutex.tla</a>
  >  PlusCalbeispiel zum FastMutex (exklusiver Ausschluss von bel. vielen Teilnehmern)

## Software

[TLA<sup>+</sup>-Toolbox](http://research.microsoft.com/en-us/um/people/lamport/tla/toolbox.html#downloading)

## Quellen

  * Leslie Lamport. <a href="http://research.microsoft.com/en-us/um/people/lamport/tla/book.html">Specifying Systems.</a> 1 edition, June 2002.</li>
  * Leslie Lamport. <a href="http://research.microsoft.com/en-us/um/people/lamport/tla/p-manual.pdf">A PlusCal User’s Manual.</a> 1.5 edition, April 2011.</li>
  * Stephan Merz. <a href="http://www.loria.fr/~merz/papers/tla+logic2008.html">The specification language tla+.</a> In Dines Bjørner and Martin C. Henson, editors, Logics of Specification Languages, Monographs in Theoretical Computer Science, pages 401–451. Springer, Berlin-Heidelberg, 2008.</li>
  * Leslie Lamport. TLA+2. October 2010.</li>
  * Christel Baier and Joost-Pieter Katoen. <a href="BK08.pdf">Principles of Model Checking.</a> MIT Press, 2008.</li>
  * Kaustuv Chaudhuri, Damien Doligez, Leslie Lamport, and Stephan Merz. A TLA+ proof system. In G. Sutcliffe, P. Rudnicki, R. Schmidt, B. Konev, and S. Schulz, editors, Proc. of the LPAR Workshop Knowledge Exchange: Automated Proversand Proof Assistants (KEAPPA’08), number 418 in CEUR Workshop Proceedings, pages17–37, 2008.
