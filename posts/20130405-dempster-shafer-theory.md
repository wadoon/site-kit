<!--
.. link:
.. description:
.. tags: mathjax
.. date: 2013/04/03
.. title: Dempster-Shafer-Theory
.. slug: 
-->

I got bored. The result is a lousy implementation of the dempster recombination
rule (dcr) in dempster-shafer theory (dct).

The dct describes system of base function to bind uncertainty to specific events
(similar to Kolgomorov axioms). But the formulation of uncertainty is a kind
easier.

Let's say a sensor says A occurred and we trust the sensor to 60 %. We can
easily model this:

$$ m(A)=0.6,m(\Omega)=0.4$$


The event got 0.6 certainty, the rest got the 0.4. Notice that A⊂Ω (That the
difference to Kolgomorov). The axioms of dct for completeness:

  1. $0 \le m(A) \le 1$ for every event A
  2. $ m(\emptyset)=0$
  3. $\sum_{A \subset \Omega} m(A) = 1$

The difference to Kolgomorov is the third axiom. In the normal probability  the
sum over every distinct events $X$ must be the sum $P(X)$:


$$P(\bigcup_i A_i = \sum_i P(A_i) $$


We can define base measures with dcr rule:


$$m_1 \oplus m_2 (A) = \begin{cases}\frac{\sum_{X \cap Y = A}
m_1(X)m_2(Y)}{1-\sum_{X \cap Y = 0} m_1(X)m_2(Y)} & else \\ 
0 & A = \emptyset 
\end{cases}
$$

Additional we can define the function Bel for the degree of believe resp. Pl for
plausibility.


$$ Bel(A) = \sum_{X \subseteq A} m(x) \qquad\qquad
   PlA) = \sum_{X \cap A \neq \emptyset} m(x)$$

It follows: $0 \le Bel(A) \le Pl(A) \le 1$.
You can divide the interval $[0,1]$ into three parts:

  * $[0,Bel(A)]$  describes certainty of event $A$
  * $[Bel(A),Pl(A)]$ describes the uncertainty of event $A$
  * $[Pl(A),1]$  describes certainty that the event $A$ does not occurred
 

Example output:

    weigla@cook ~ % python drc.py
	A: [m: 0.680000] [Bel 0.680000] [Pl 1.000000] ▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒
    B: [m: 0.000000] [Bel 0.000000] [Pl 0.320000] ▒▒▒▒▒▒░░░░░░░░░░░░░░
    C: [m: 0.000000] [Bel 0.000000] [Pl 0.320000] ▒▒▒▒▒▒░░░░░░░░░░░░░░
    O: [m: 0.320000] [Bel 1.000000] [Pl 1.000000] ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

    A: [m: 0.438596] [Bel 0.438596] [Pl 0.438596] ▓▓▓▓▓▓▓▓░░░░░░░░░░░░
    B: [m: 0.210526] [Bel 0.000000] [Pl 0.000000] ░░░░░░░░░░░░░░░░░░░░
    C: [m: 0.350877] [Bel 0.000000] [Pl 0.000000] ░░░░░░░░░░░░░░░░░░░░
    O: [m: 0.000000] [Bel 0.438596] [Pl 0.438596] ▓▓▓▓▓▓▓▓░░░░░░░░░░░░



drc.py:

    #-*- encoding: utf-8 -*- 

	class DictWrap(dict):
		def __call__(self,key): return self[key]

	def drc(m1,m2):
		def appl(A):
			K = sum((m1(X)*m2(Y)
                    for X in m1.keys()
                    for Y in m2.keys()
                    if len(X&Y) == 0))    
            if A:
                s = sum(( m1(X)*m2(Y)
                          for X in m1.keys()
                          for Y in m2.keys()
                          if X&Y == A))            
                return s/(1-K)
            else:
                return 0
        appl.keys = m1.keys
        return appl


    def Pl(m, event):
        return sum( [m(X) for X in m.keys() 
                         if len(X & event) > 0])

    def Bel(m,event):
        return sum( [m(X) for X in m.keys() 
                         if X <= event])

    #events 
    A = frozenset(('A',))
    B = frozenset(('B',))
    C = frozenset(('C',))
    OMEGA = A | B | C

    #example: two sensors
	s1 = DictWrap({ A : 0.6, OMEGA: 0.4}) # s1 mesaures A with certainty of 60%
	s2 = DictWrap({ A : 0.2, OMEGA: 0.8}) # s2 mesaures A with certainty of 20%

    #combine
    fusion = drc(s1,s2)
    def show(text, event):
        print '%s: [m: %f] [Bel %f] [Pl %f]' % (text, 
                                           fusion(event),
                                           Bel(fusion,event), 
                                           Pl(fusion,event)),
        print_bar(Bel(fusion,event), Pl(fusion,event))
    
    from math import ceil as round

    def print_bar(bel, pl, width = 20):
        fbel = int(width * bel)
        fpl = int(width * pl)
    
    a = fbel 
    b = fpl - fbel 
    c = width - fpl 
    print ('▓' * a) + ('▒' * b) + ('░' * c) 
    
    show('A', A); show('B', B); show('C', C); show('O', OMEGA)

    #combine 
    s3 = DictWrap({ A: 0.2, B: 0.3, C: 0.5})
    fusion = drc(fusion,s3)

    show('A', A); show('B', B); show('C', C); show('O', OMEGA)
