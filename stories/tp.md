<!--
	.. title: Teamprojekt - Extraktion von Personenbezeziehungen aus juristischen Texten
	.. subtitle: Extraction of person relationships in legally texts
    .. author: Alexander Weigl
    .. date: 2011/11/01
-->

## Abstract 


>  Die Beziehungsdarstellung innerhalb juristischen Texten ist sehr komplex.
>  Im Rahmen eines Teamprojekt wurde nun Konzept zur Extraktion und
>  Darstellung dieser Beziehungen erarbeitet.
>  Es stützt sich auf Regeln, die aus deutsche jur. Texten abgeleitet und verifiziert wurden.
>  Eine Implementierung erfolgte in Lisp und wird vom C.~H. Beck Verlag eingesetzt.


>  The presentation of relationships within legal texts is complex.
>  A concept for extraction and visualization was developed during a team project.
>  It is based on rules that was derived and verified from german legal texts.
>  We created an implemenation an Lisp, that is used by C. H. Beck Verlag.


## Table of contents

	1 Einleitung
	1.1 Problemstellung 
		1.2 Aufgabenstellung
	2 Modell
		2.1 Textaufbereitung 
		2.2 Personen erkennen 
		2.2.1 Personen finden
			2.2.2 Gleichheit von Personen 
			2.2.3 Pronomen auflösen
			2.3 Beziehungserkennung
				2.3.1 Ansatz 1: Erkennen von Wörtergruppen 
				2.3.2 Ansatz 2: Anzahl von Wörter und Personen 
				2.3.3 Ansatz 3: Regelbäume
			2.4 Zusammenfassung des Modells
	3 Implementierung 
		3.1 Datenmodell 
			3.1.1 Personen 
			3.1.2 Wörter, Sätze und Referenzen 
		3.2 Algorithmen in Lisp
			3.2.1 Tokenize 
			3.2.2 Find-Person 
			3.2.3 Merge-Person 
			3.2.4 Dissolve-Pronoun 
			3.2.5 Find-Relation: 1. Ansatz Wörtergruppen 
			3.2.6 Find-Relation: Anlauf 2: Anzahl von Wörter und Personen 
			3.2.7 Find-Relation: Anlauf 3: Regelbaum 
		3.3 Visualisierung
			3.3.1 Relationenfilter
			3.3.2 Graph aufbauen und rendern
	4 Evaluation 
		4.1 Evaluationsumgebung 
		4.2 Auswertung 
	5 Diskussion 
		5.1 Kritische Worte 
		5.2 Offene Ideen 
	6 Schlussbetrachtung 
	A Verwendung der Software 
		A.1 Ordnerstruktur und Dateien 
		A.2 Softwareeinsatz 
	Literatur 
