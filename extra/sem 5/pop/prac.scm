(define (squre x) (* x x))
(define (sum x y) (+ (squre x) ()))


sci--------------------

(define (mid-point a) 
	(cons (/ (+ (car (car a)) (car (cdr a))) 2) (/ (+ (car(cdr (car a))) (car(cdr(cdr a))) ) 2))) 






 (define (make-segment p q)(cons (make-point (car p) (cdr p)) (make-point (car q) (cdr q))))


 (define (make-point x y) (cons x y))

 (define (x-point p) (car p))

(define (y-point) ( cdr p))

 (define (start-point a b) ( make-point a b))

 (define (end-point a b) (make-point a b))



 (define (list-ref items n)
(if (= n 1)
(car items)
(list-ref (cdr items) (- n 1))))



(define (length items)
(if (null? items)
0
(+ 1 (length (cdr items)))))

(define (pp length)
	'(1 2 3 4))



(define (length items)
(define (length-iter a count)
(if (null? a)
count
(length-iter (cdr a) (+ 1 count))))
(length-iter items 0))


(define (append1 l1 l2)
	(cond ((null?  l1) l2)
		(else(cons (car l1) (append1 (cdr l1)  l2)))))


(define (last-pair l acc)
	(cond ((null? l) acc )
		(else (last-pair (cdr l) (car l)))))

(define (reverse l )
	(cond ((null? l) l)
		(else (cons (reverse (cdr l)) (car l)))))


(define (reverse l)
	(cond ((null? l) l)
		(else (cons (list-ref (car l)) (reverse  list-ref (cdr l))))))

(define (squre x) (* x x))
(define (squre-tree l)
	(cond ((null? l) l)
		((not(pair? (car l)))(cons (squre (car l)) (squre-tree (cdr l))))
		(else(cons (squre (squre-tree (car l))
			(squre-tree (cdr l)))))))

(define (squre-tree l)
	(cond ((null? l)l)
	((not (pair? (car l))) (cons (map (lambda(x) (* x x)) (car l)) (squre-tree (cdr l))))
	(else (cons (map (lambda (x) (* x x)) (car l)) 
		(map (lambda (x) (* x x)) (cdr l))))))
(define (map proc l)
	(cond ((null? l) l)
	(else (cons (proc (car l)) (map proc (cdr l))))))

(define (set-to-wow! x)
(set-car! x 'wow)
x)

(define (cons x y)
(define (dispatch m)
(cond ((eq? m 'car) x)
((eq? m 'cdr) y)
(else (error "Undefined operation -- CONS" m))))
dispatch)


(define (car z) (z 'car))
(define (cdr z) (z 'cdr))




(define (even? l)
		(cond ((null? l) '())
			  ((= (modulo (car l) 2) 0) (cons (car l) (even? (cdr l))))
		      (else(even? (cdr l) )) 
		      )
		)
	(define (curry-filter even?)
		(lambda(m) (even? m)))



(define (procwith3args x a b)
	(* x (+ a b)))
(define (curry pro)
	(lambda(p) (lambda (q) (lambda(r) (pro p q r)))))


(define (variable? x)
	(if(symbol? x) #t
		#f))

(define (deriv exp var)
	(cond((number? exp) 0)
		((variable? exp) 1)
		((sum? exp) (+ (deriv (cadr exp) var) (deriv (caddr exp) var)))
		((product? exp) (+ (* (cadr exp) (deriv (caddr exp) var)) (* (caddr exp) (deriv (cadr exp) var))))
		((divide? exp)(/ (- (* (caddr exp) (deriv (cadr exp) var)) (* (cadr) (deriv (caddr exp) var))) (squre (caddr exp))))
		((ex? exp)
				(if(number? (cadr exp))
					(* (ex (cadr exp) (caddr exp)) (* 'log (cadr exp)))
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

(define (variable? e)
	(if(number? e)#f
		#t))

(define (ex? e)
	(if (eq? (car e) '^) #t
	#f ))
(define (con? e)
	(if(number? (car (cdr e))) #t
		#f))

; (define (ex x n)
; 	(cond ( (= n 0) 1 
; 		   )
; 	 ( (= (modulo n 2) 0)  (* (ex x (/ n 2)) (ex x (/ n 2)))
; 	 )
; 	 (else (* x (ex x (- n 1))
; 	 		)
; 	 )
; 	 )
; )

(define (exvar x n)
	(cond((= n 0) 1)
		(else( cons ^ (cons x n)))))