(define (attach-type tag l)
	(cons tag l))

(define (insert time  action)
	(cons time action))

(define (inctime acc)
	(+ acc 1))

(define (insert-queue time action)
	 (cons (car time) action))

(define (make-pqueue l acc)
	(cond((null? l)l)
		(else (let ((queue (list acc)))
					(cons (cons (car queue) (car l)) (make-pqueue (cdr l) (inctime acc)))
					))))

(define (action1 l)
		(begin (display(car (car l)))
			(display "  ")
			(cdr l))
	)
(define (current-time l)
	(car (car l)))

(define (apply l)
		(cond((null? l)l)
			(else(cons (cons (+ (car (car l)) 1) (cdr (car l))) (apply (cdr l))))))

	(define (new pos l acc count)
		(cond ((null? l) (cons (cons (+ acc 1) (pqueue count)) l))
			((= pos acc) (cons (cons (current-time l) (pqueue count)) (apply l)))
			(else(cons (car l) (new pos (cdr l) (+ acc 1) count)))
		))

(define (pqueue count)
	(if(= (modulo count 5) 0) 2
		1
		))
(define (update l)
	(define (update1 l acc) 
		(cond ((null? l) l)
	(else (cons (cons acc (cdr (car l))) (update1 (cdr l) (+ acc 1))))))
		(update1 l 0))


(define (print x)
	(display x))


(define (action2 l acc)
	(cond((null? l)l)
		(else (begin 
				(display(car (car l)))
				(display "  ")
				(new (+ (caar l) 3) (cdr l) (caar l) acc)
				)
		)))

(define (extractlist l acc)
	(cond((null? l) l)
		((= (cdr (car l)) 1)
			(action1 l))
		(else (action2 l acc))))


(define (ret l)
	(define (return l acc)
		(cond ((or (null? l) (= acc 500)))
				(else(return (extractlist l acc) (+ acc 1)))))
			(return l 0))

(ret (make-pqueue '(2 2 2 2 2) 0))
