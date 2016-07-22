
		(define (procwith3args x a b)
					(* x (+ a b)))
		(define (curry pro)
					(lambda(p) (lambda (q) (lambda(r) (pro p q r))))


	(define (even? l)
		(cond ((null? l) '())
			  ((= (modulo (car l) 2) 0) (cons (car l) (even? (cdr l))))
		      (else(even? (cdr l) )) 
		      )
		)
	(define (curry-filter e)
		(lambda(m) (e m)))
((curried-filter even?) '(1 2 3))


