(define (isqrt guess x) 
	(if(good-enough? guess x)
 			guess
			(isqrt (improve-guess guess x) x)
	)
)

(define (good-enough? guess x)
	(< (abs (- (squre guess) x)) 0.001))

(define (improve-guess guess x)
	(/ (+ guess (/ x guess)) 2))	


(define (fib n)
	(cond ((= n 0) 0)
			((= n 1)1)
			(else (+ (fib (- n 1)) (fib (- n 2))))))	

(define (ifib n a)
	(if(= n 0) 0)
	if(= n 1) 1
	(ifib (- n 1) ))



(define (ifib a b count)
(if(= count 0)
	b
	(ifib (+ a b) a (- count 1))))


(define (sum x y)
	(lambda(x y)  (+ x y)))

(define (squre x) (* x x) )


(define (ex x n)
	(cond ( (= n 0) 1 
		   )
	 ( (= (modulo n 2) 0)  (* (ex x (/ n 2)) (ex x (/ n 2)))
	 )
	 (else (* x (ex x (- n 1))
	 		)
	 )
	 )
)



(define (exitr  x n acc)
	(cond ( (= n 0) 
			acc 
		   )
	 ( (= (modulo n 2) 0) 
	 	( exitr x (/ n 2) (* acc (exitr x (/ n 2) 1) )))
	 (else ((exitr x (- n 1) (* acc x))-1) 
	 )))
	 
(define (len n )
(- (ex 2 n) 1))



(define (insertL new old l )
	(cond ((null? l) '())
			((= (car l) old) (cons new  l)) 
			
	(else (cons (car l) (insertL new old (cdr l) ) )
	)))


(define (count-occur str l acc)

(cond ((null? l) acc) 
       (( string=? str (car l)) (count-occur str (cdr l) (+ acc 1)) ) 
       (else(count-occur str (cdr l)  acc ))))




(define (num-count l acc num list)
(cond  ((null? l) '())
		(if(= num (car l))(num-count (cdr l) (+ acc 1) num list))
		(else(if(!= num (car l)) (cons list (cons (num acc)))
		(num-count (cdr l))))
)))


(define (count x l acc) 
(cond ((null? l) acc)
 ((= x (car l)) (count x (cdr l) (+ acc 1)))
  (else )))

(define (count-rep l)
 (cond ( (null? l) '() ) 
 (else 
 (cons (cons (car l) (count (car l) l 0)) 
 (count-rep (remove (car l) l) )) 
 )
 )
 )

(define (remove x l)
( cond 
 ((null? l) '() )
 (= x (car l) )
  (remove x (cdr l)) ) 
  (else l) 
  )


  (define (count x l acc) (cond ((null? l) acc) ((= x (car l)) (count x (cdr l) (+ acc 1)) )  (else acc)   ) )

(define (count-rep l) (cond ( (null? l) '() ) 
 (else (cons (cons (car l) (count (car l) l 0)) (count-rep (remove (car l) l) ))     ))

(define (remove x l)( cond  ((null? l) '() ) (= x (car l) ) (remove x (cdr l)) ) (else l) ))


(define (count x l acc) (cond ((null? l) acc) ((= x (car l)) (count x (cdr l) (+ acc 1)) )  (else acc)   ) )

(define (count-rep l) (cond ( (null? l) '() ) 
 (else (cons (cons (car l) (count (car l) l 0)) (count-rep (remove (car l) l) ))     ))

(define (remove x l)( cond  ((null? l) '() ) ((= x (car l) ) (remove x (cdr l)) ) (else l) ))



