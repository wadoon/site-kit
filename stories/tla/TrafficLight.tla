---------------------------- MODULE TrafficLight ----------------------------
EXTENDS  Naturals , TLC
VARIABLE red,yellow,green

vars   == << red , yellow , green>>
Boolean == { TRUE, FALSE }

TypeInvariant == \/ red    \in Boolean 
                 \/ yellow \in Boolean
                 \/ green \in Boolean
                    

SafetyProperty ==  /\ \neg (red /\ green)      \* Grün/Rot darf nicht leuchten 
                   /\ \neg (yellow /\ green)   \* Grün/Gelb darf nicht leuchten
                   /\ (red \/ green \/ yellow) \* mind. eine Lampe leuchtet
                   

-----------------------------------------------------------------------------

(* Umschalten von Grün auf Rot.*)
PreStop == /\ ( green /\ \neg yellow /\ \neg red ) \* ENABLING CONDITION           
           /\ green'  = FALSE
           /\ yellow' = TRUE
           /\ red'    = TRUE 
           
FinStop == /\ ( \neg green /\ yellow /\ red ) \* ENABLING CONDITION
           /\ UNCHANGED << green, red >>
           /\ yellow' = FALSE

-----------------------------------------------------------------------------

(* Umschalten von Rot auf Grün.*)
PreGo == /\ ( \neg green /\ \neg yellow /\  red ) \* ENABLING CONDITION           
           /\ green'  = FALSE
           /\ yellow' = TRUE
           /\ red'    = FALSE 
           
FinGo == /\ ( \neg green /\ yellow /\ \neg red ) \* ENABLING CONDITION
           /\ UNCHANGED  red
           /\ yellow' = FALSE
           /\ green' = TRUE
           
-----------------------------------------------------------------------------
Go   == green /\ \neg red /\ \neg yellow
Stop == \neg green /\  red /\  yellow


LivProperty == /\ []<>Go 
               /\ []<>Stop

Fairness    == WF_vars(FinGo \/ FinStop)        
        
Init == /\ red \in Boolean 
        /\ yellow \in Boolean 
        /\ green \in Boolean 
        /\ SafetyProperty
           
Next == \/ PreStop
        \/ PreGo
        \/ FinStop
        \/ FinGo
        
                
Spec == Init /\ [][Next]_vars /\ Fairness
           
=============================================================================
\* Modification History
\* Last modified Tue Jan 03 10:44:48 CET 2012 by weigla
\* Created Tue Jan 03 10:25:30 CET 2012 by weigla
