(echo "starting Z3...")
(declare-const p Bool)
(declare-const q Bool)
(assert (=> (and p q) p))
(assert (=> p (and p q)))
(assert (=> p q))
(check-sat)
(get-model)
; Solution : p = False, q = False