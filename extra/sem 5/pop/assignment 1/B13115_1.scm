2.1:-(define (fib-recur n) (cond ((= n 0) 0) ((= n 1) 1) (else  (+ (fib-recur (- n 1)) (fib-recur (- n 2)))))) 

2.2:-(define (fib-iter curr next n) ( cond ((= n 1) next) (else (fib-iter next (+ curr next) (- n 1)))))

3.1:-(define (exp-recur x n) (cond ((= n 0) 1) ((iseven? n) (square (exp-recur x (/ n 2)))) (else (* (square (exp-recur x (/ n 2))) x) )))

	(define (square x ) (* x x))

	(define (iseven? x) (cond ((= 0 (modulo x 2)) #t) (else #f)))

3.2:-(define (exp-iter x n acc) (cond  ((= n 0) acc ) ( (iseven? n) (exp-iter (square x) (/ n 2) acc) ) (else  (exp-iter x (- n 1) (* x acc)))))

4:-(define (accumulate combiner null-value term a next b)  (cond ((or (= a b) (> a b)) null-value)
			 ( (=? combiner +) (accumulate combiner (+ null-value (exp-recur a term)) term (+ a next) next b) ) 
			  ( (=? combiner *) (accumulate combiner (* null-value (exp-recur a term)) term (+ a next) next b) ) ))



5:-(define (insertL new old l) (cond ((null? l) '()) ((= old (car l)) (cons new l)) (else (cons (car l) (insertL new old (cdr l))) )))


6:-(define (count-occur str l) (fold (lambda(acc x) (if (string=? str x) (+ acc 1) acc)) 0 l))

7.1:-(define (fold f acc l) (cond ((null? l) acc) ( else (fold f (f acc (car l)) (cdr l) ))))

7.2:-(define (filter f l)( cond ((null? l) '()) (else (if (f (cdr l)) (cons (car l) (filter (cdr l))) (filter (cdr l)) )) ))

8:-(define (longest-stringNear l) (fold (lambda(acc x) (if (> (string-length x) (string-length acc)) x acc )) "" l))

9:-(define (longest-stringfar l) (fold (lambda(acc x) (if (or  (= (string-length x) (string-length acc)) (> (string-length x) (string-length acc))) x acc )) "" l))


10:-(define (check-duplicates l) (cond ((null? l) #f) ((and (if (> (count-occur (car l) l) 1) #t #f) (check-duplicates (cdr l))) #f) (else #t) ))





