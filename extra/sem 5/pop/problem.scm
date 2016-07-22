


(define (sumlist l1 l2)
	(cond((null? l1) l2)
		((null? l2)l1)
		(else(cons (+ (car l1) (car l2)) (sumlist (cdr l1) (cdr l2))))
		)
	)

(define x '(2 2 3 4))
(define y '(1 2 3 4 4 45))
(sumlist '() '())
