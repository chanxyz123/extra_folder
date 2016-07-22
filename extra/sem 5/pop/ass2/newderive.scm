(define (deriv exp var)
	(cond((number? exp) 0)
		((and (atom? exp)(diffvar? exp var)) 0)
		((variable? exp var) 1)
		((sum? exp) (makesum (deriv (cadr exp) var) (deriv (caddr exp) var)))
		((product? exp) (makesum (makeproduct (cadr exp) (deriv (caddr exp) var)) (makeproduct (caddr exp) (deriv (cadr exp) var))))
		((divide? exp)(list '/ (cons '- (cons (cons '* (cons (caddr exp) (deriv (cadr exp) var)))  (cons '* (cons (cadr exp) (deriv (caddr exp) var)))))  (square (caddr exp))))
		((ex? exp)
				(if(number? (cadr exp))
					( makeproduct (ex (cadr exp) (caddr exp)) (cons 'log (cadr exp)) )
					( makeproduct (makeproduct (caddr exp)  (exvar (cadr exp) (- (caddr exp) 1))) (deriv (cadr exp) var)) ) )))

(define (makesum exp1 exp2)
	(cond((= exp1 0) exp2)
		((= exp2 0) exp1)
		((and (number? exp1) (number? exp2)) (+ exp1 exp2))
		(else (list '+ exp1 exp2))))

(define (makeproduct exp1 exp2)
	(cond((and (number? exp1) (number? exp2)) (* exp1 exp2))
		((number? exp1) 
				(cond ((= exp1 0) 0)
						((= exp1 1) exp2)))
		((number? exp2) 
				(cond ((= exp2 0) 0)
						((= exp2 1) exp1)))		
		(else (list '* exp1 exp2))))

(define (atom? x) (not (or (pair? x) (null? x))))

(define (sum? e)
	(if(eq? (car e) '+) #t
		#f))

(define (product? e)
	(if(eq? (car e) '*)#t
		#f))

(define (divide? e)
	(if(eq? (car e) '/) #t
		#f))

(define (variable? e v)
	(if(not(eq? e v))#f
		#t))

(define (diffvar? e v)
	(if(not(eq? e v))#t
		#f))

(define (ex? e)
	(if (eq? (car e) '^) #t
	#f ))
(define (con? e)
	(if(number? (car (cdr e))) #t
		#f))

(define (ex n x)
	(cons '^ (cons n x)))


(define (exvar x n)
	(cond((= n 0) 1)
		((= n 1) x)
		(else( cons '^ (cons x n)))))

(define (square x)
	(exvar x 2)) 

(deriv '(+ x 1) 'x)
(deriv '(+ x x) 'x)
(deriv '(* x y) 'x)
(deriv '(^ 2 x) 'x)
(deriv '(^ x 2) 'x)