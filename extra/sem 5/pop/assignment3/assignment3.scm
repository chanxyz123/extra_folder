(define (attach-type tag l)
	(cons tag l))

(define (insert-queue time action)
	 (cons (car time) action))

(define (pmake l acc)
	(cond((null? l)l)
		(else (let ((queue (list acc)))
					(cons (cons (car queue) (car l)) (pmake (cdr l) (+ acc 1)))
					))))

(define (a1 l)
		(begin (display(car (car l)))
			(display "  ")
			(cdr l))
	)
(define (current-time l)
	(car (car l)))

(define (apply l)
		(cond((null? l)l)
			(else(cons (cons (+ (car (car l)) 1) (cdr (car l))) (apply (cdr l))))))

	(define (new pos l acc)
		(cond ((null? l) (cons (cons (+ acc 1) 1) l))
			((= pos acc) (cons (cons (current-time l) 1) (apply l)))
			(else(cons (car l) (new pos (cdr l) (+ acc 1))))
		))


(define (up l)
	(define (up1 l acc) 
		(cond ((null? l) l)
	(else (cons (cons acc (cdr (car l))) (up1 (cdr l) (+ acc 1))))))
		(up1 l 0))

(define (a2 l)
	(cond((null? l)l)
		(else (begin 
				(display(car (car l)))
				(display "  ")
				(new (+ (caar l) 3) (cdr l) (caar l))
				)
		)))

(define (extractelement l)
	(cond((null? l) l)
		((= (cdr (car l)) 1)
			(a1 l))
		(else (a2 l))))


(define (ret l)
	(define (return l acc)
		(cond ((or (null? l) (= acc 500)))
				(else(return (extractelement l) (+ acc 1)))))
			(return l 0))

(ret (pmake '(2 2 2 2 2 2 1 1 2 2 1 2 2 1 1 2 1 2 2) 0))
