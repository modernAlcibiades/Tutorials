; Changes based on Reviewer comments
(declare-const p Bool)
(declare-const q Bool)
(define-fun conjecture () Bool
	(= (= p (and p q))
		(=> p q)))
(assert (not conjecture))
(check-sat)
; Checking equivalence of two equations by getting unsat on negation
; Answer : the two equations are equivalent