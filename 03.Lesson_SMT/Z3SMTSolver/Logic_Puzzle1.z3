(echo "starting Z3...")
(declare-const x Int)
(declare-const y Int)
(declare-const z Int)
(assert (= (* 2 x) 10))
(assert (= (+ (* x y) y) 12))
(assert (= (- (* x y) (* z x)) x))
(check-sat)
(get-model)
//Solution : z = 1