
	(define (even? l)
		(cond ((null? l) '())
			  ((= (modulo (car l) 2) 0) (cons (car l) (even? (cdr l))))
		      (else(even? (cdr l) )) 
		      )
		)
	(define (curried-filter e)
		(lambda(m) (e m)))

((curried-filter even?) '(1 2 3))