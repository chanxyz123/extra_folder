
		(define (procwith3args x a b)
					(* x (+ a b)))
		(define (curry pro)
					(lambda(p) (lambda (q) (lambda(r) (pro p q r)))))

((((curry procwith3args) 3) 4) 5)
