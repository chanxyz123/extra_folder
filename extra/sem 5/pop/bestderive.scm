(define (deriv exp var)
	(cond((number? exp) 0)
		((and (atom? exp)(diffvar? exp var)) 0)
		((variable? exp var) 1)
		((sum? exp)
		  (if(null? (cdr exp)) 0
		  (makesum (deriv (cadr exp) var) (deriv (cons '+ (cddr exp)) var))))
		((product? exp)
		(if(null? (cdddr exp))
			(makesum (makeproduct (cons (deriv (caddr exp) var) (cadr exp))) (makeproduct (cons (caddr exp) (deriv (cadr exp) var)))) 
			(makesum (makeproduct (cons (deriv (cadr exp) var) (cddr exp))) (makeproduct (cons (cadr exp) (deriv (cons '* (cddr exp)) var))))))
		((divide? exp)(list '/ (cons '- (cons (cons '* (cons (caddr exp) (deriv (cadr exp) var)))  (cons '* (cons (cadr exp) (deriv (caddr exp) var)))))  (square (caddr exp))))
		((ex? exp)
				(if(number? (cadr exp))
					( list '* (ex (cadr exp) (caddr exp)) (cons 'log (cadr exp)) )
					( list '* (caddr exp)  (exvar (cadr exp) (- (caddr exp) 1)) (deriv (cadr exp) var) )))))

(define (makesum exp1 exp2)
	(cond((= exp1 0) exp2)
		((= exp2 0) exp1)
		((and (number? exp1) (number? exp2)) (+ exp1 exp2))
		(else (list '+ exp1 exp2))))

(define (makeproduct l)
	(cond ((null? l) 1)
			((number? (car l)) 
				(cond ((= (car l) 0) 0)
						((= (car l) 1) 1) 
						(else (* (car l) (makeproduct (cdr l))))))
		  (else (list '* (car l) (makeproduct (cdr l))))))

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
(deriv '(+ x x x) 'x)
(deriv '(* x 3) 'x)
; (deriv '(* x x x) 'x)