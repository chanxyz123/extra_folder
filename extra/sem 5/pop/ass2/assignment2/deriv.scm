(define (derivar E var)
	(cond((number? E) 0)
		((and (atom? E)(diffvar? E var)) 0)
		((varariable? E var) 1)
		((sum? E) (makesum (derivar (cadr E) var) (derivar (caddr E) var)))
		((product? E) (makesum (makeproduct (cadr E) (derivar (caddr E) var)) (makeproduct (caddr E) (derivar (cadr E) var))))
		((divaride? E)(makedivaride (makediff (makeproduct (caddr E) (derivar (cadr E) var))  (makeproduct (cadr E) (derivar (caddr E) var))) (square (caddr E))))
		((ex? E)
				(if(number? (cadr E))
					( makeproduct (makeproduct (ex (cadr E) (caddr E)) (cons 'log (cadr E))) (derivar (caddr E) var))
					( makeproduct (makeproduct (caddr E)  (exvar (cadr E) (- (caddr E) 1))) (derivar (cadr E) var)) ))))



(define (makedivaride exp exp2)
	(cond((and (number? exp) (number? exp2)) (/ exp exp2))
		((number? exp) 
				(cond ((= exp 0) 0)
				(else (list '/ exp exp2))))

		((number? exp2) 
				(cond ((= exp2 1) exp)
				(else (list '/ exp exp2))))		
		(else (if (eq? exp exp2) 1
			(list '/ exp exp2)))))

(define (makediff exp exp2)
	(cond((and (number? exp) (number? exp2)) (- exp exp2))
		((number? exp) 
				(cond ((= exp 0) (cons '- exp2))
				(else (list '- exp exp2))))
		((number? exp2) 
				(cond ((= exp2 0) exp)
				(else (list '- exp exp2))))
		(else (if (eq? exp exp2) 0
			(list '- exp exp2)))))

(define (makesum exp exp2)
	(cond((and (number? exp) (number? exp2)) (+ exp exp2))
		((number? exp) 
				(cond ((= exp 0) exp2)
				(else (list '+ exp exp2))))
		((number? exp2) 
				(cond ((= exp2 0) exp)
				(else (list '+ exp exp2))))		
		(else (list '+ exp exp2))))
(define (makeproduct exp exp2)
	(cond((and (number? exp) (number? exp2)) (* exp exp2))
		((number? exp) 
				(cond ((= exp 0) 0)
						((= exp 1) exp2)
				(else (list '* exp exp2))))
		((number? exp2) 
				(cond ((= exp2 0) 0)
						((= exp2 1) exp)
				(else (list '* exp exp2))))		
		(else (list '* exp exp2))))

(define (atom? x) (not (or (pair? x) (null? x))))

(define (sum? e)
	(if(eq? (car e) '+) #t
		#f))

(define (product? e)
	(if(eq? (car e) '*)#t
		#f))

(define (divaride? e)
	(if(eq? (car e) '/) #t
		#f))

(define (varariable? e var)
	(if(not(eq? e var))#f
		#t))

(define (diffvar? e var)
	(if(not(eq? e var))#t
		#f))

(define (ex? e)
	(if (eq? (car e) '^) #t
	#f ))

(define (ex n x)
	(cons '^ (cons n x)))


(define (exvar x n)
	(cond((= n 0) 1)
		((= n 1) x)
		(else( cons '^ (cons x n)))))

(define (square x)
	(exvar x 2)) 

(derivar '(+ (^ (+ x (* x x)) 2) 1) 'x)
(derivar '(+ (^ (+ x (* x x)) 2) x) 'x)
(derivar '(* (^ (+ x (* x x)) 2) y) 'x)
(derivar '(/ (^ (+ x (* x x)) 2) x) 'x)
(derivar '(^ 2 (+ x (^ (+ x (* x x)) 2))) 'x)
(derivar '(^ (+ x (* x x)) 2) 'x)