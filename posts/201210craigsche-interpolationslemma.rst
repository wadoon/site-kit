.. title: Craig'sche Interpolation Lemma
.. date: 2012/10/18
.. slug:
.. tags: mathjax


**Satz:**
Seien $A,B$ zwei aussagenlogische Formeln und es gilt :math:`\models A \Rightarrow B` (Tautologie), dann existiert eine aussagenlogische Formeln $C$, sodass

.. math:: \models A \Rightarrow C \text{ und } \models C \Rightarrow B

wobei $C$ nur aus Konstanten $w,f$ und gemeinsamen Atome von $A,B$ besteht.

*Beispiel:* Nehmen wir an, dass :math:`A := p \wedge q` 
und :math:`B:= q \vee r`. Dann ist  $C := q$.

Testen wir die Tautologien:

.. math:: p \wedge q \Rightarrow q \equiv  \neg p \vee \neg q \vee q \equiv w

.. math:: q  \Rightarrow q \vee r \equiv  \neg q \vee q \vee r \equiv w 

*Beweis (konstrutiv):*

*Erster Teil* ($\models A \Rightarrow C$). Sei $C$ eine Disjunktion wie folgt:

.. math::  C := \bigvee A[c_1,\ldots, c_n] 

dabei ersetzen wir die Atome :math:`P_1, \ldots, P_n` aus $A$, die *nicht* in $B$ vorkommen durch alle möglichen Kombinationen von Konstanten :math:`c_1,\ldots,c_n \in \{w,f\}`. Für jede Interpretation $I$ mit $val_I(A) = w$ gilt: $val_I(C)=w$. Denn in der Disjunktion $C$ taucht jede mögliche Kombination der Wahrheitswerte von $P_i$ auf. Der Term der Disjunktion der $C$ wahr macht ist dieser mit:

.. math::  A[c_1, \ldots, c_n] \text{ mit } c_i = val_I(P_i)  

*Zweiter Teil* (:math:`\models C \Rightarrow B`).

Sei $I$ eine Interpretation mit $val_I(C) = w$. Dann ist mind. ein Term der
Disjunktion wahr. Wir konstruieren eine Hilfeinterpretation $J$ wie folgt:


.. math::
          
    J(P) = 	\begin{cases}
		c_i & \colon  P = P_i \text{ für } 1\le i \le n \\
		I(P) & \colon \text{ sonst}
		\end{cases}


$J$ ist ein Modell von $C$ und $A$. Nach Vorrausetzung (:math:`A \Rightarrow B`) folgt
$val_J(B) = w$. Für alle Atome in $B$ trifft die Interpretation $J$ die gleiche
Aussage wie $I$. ($P_i$ waren die Atome aus :math:`P_i \in A \wedge P_i \notin B`).
Also folgt $val_I(B) = w$. 


**Beispiel:** Zurück zu unseren Beispiel. Wie konstruieren das $C$ nun nachdem
Beweis.

.. math::	 C := A[p=0] \vee A[p=1] \equiv (0 \wedge q) \vee (1 \wedge q) \equiv q
