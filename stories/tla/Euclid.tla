(* --algorithm EuclidAlg
    variables u = 24; v \in 1 .. N , v_in = v
    begin print << u , v >>;
    while u # 0 do
        if u < v then 
            u := v || v := u;
        end if;
        u := u - v;
    end while;
    assert v = gcd(u,v_in);
    end algorithm *)
------------------------------- MODULE Euclid -------------------------------
EXTENDS Naturals, TLC
CONSTANT N

gcd(x,y) == CHOOSE i \in 1..x : 
               /\ x % i = 0
               /\ y % i = 0
               /\ \A j \in 1 .. x: 
                      /\ x % i = 0
                      /\ y % i = 0
                      /\ i <= j

\* BEGIN TRANSLATION
VARIABLES u, v, v_in, pc

vars == << u, v, v_in, pc >>

Init == (* Global variables *)
        /\ u = 24
        /\ v \in 1 .. N
        /\ v_in = v
        /\ pc = "Lbl_1"

Lbl_1 == /\ pc = "Lbl_1"
         /\ PrintT(<< u , v >>)
         /\ pc' = "Lbl_2"
         /\ UNCHANGED << u, v, v_in >>

Lbl_2 == /\ pc = "Lbl_2"
         /\ IF u # 0
               THEN /\ IF u < v
                          THEN /\ /\ u' = v
                                  /\ v' = u
                          ELSE /\ TRUE
                               /\ UNCHANGED << u, v >>
                    /\ pc' = "Lbl_3"
               ELSE /\ Assert(v = gcd(24,v_in), 
                              "Failure of assertion at line 10, column 5.")
                    /\ pc' = "Done"
                    /\ UNCHANGED << u, v >>
         /\ v_in' = v_in

Lbl_3 == /\ pc = "Lbl_3"
         /\ u' = u - v
         /\ pc' = "Lbl_2"
         /\ UNCHANGED << v, v_in >>

Next == Lbl_1 \/ Lbl_2 \/ Lbl_3
           \/ (* Disjunct to prevent deadlock on termination *)
              (pc = "Done" /\ UNCHANGED vars)

Spec == Init /\ [][Next]_vars

Termination == <>(pc = "Done")

\* END TRANSLATION
 

=============================================================================
\* Modification History
\* Last modified Fri Dec 30 03:48:38 CET 2011 by weigla
\* Created Fri Oct 28 15:56:36 CEST 2011 by weigla
