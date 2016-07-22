(define (deriv exp var)
	(cond((number? exp) 0)
		((variable? exp var) 1)
		((sum? exp) (list '+ (deriv (cadr exp) var) (deriv (caddr exp) var)))
		((product? exp) (list '+ (cons '* (cons (cadr exp) (deriv (caddr exp) var))) (cons'* (cons(caddr exp) (deriv (cadr exp) var)))))
		((divide? exp)(list '/ (cons '- (cons (cons '* (cons (caddr exp) (deriv (cadr exp) var)))  (cons '* (cons (cadr exp) (deriv (caddr exp) var)))))  (square (caddr exp))))
		((ex? exp)
				(if(number? (cadr exp))
					( list '* (ex (cadr exp) (caddr exp)) (cons 'log (cadr exp)) )
					( list '* (caddr exp)  (exvar (cadr exp) (- (caddr exp) 1)) (deriv (cadr exp) var) )))))
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
	(if(not(equal? e v))#f
		#t))

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









; (deriv '(^ y 2) 'y)
;(deriv '(^ 2 y) 'y)

(deriv '(+ x 1) 'x)
(deriv '(* x 4) 'x)
(deriv '(/ (^ x 2) x) 'x) 