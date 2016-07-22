(define (add-stream l1 acc)
	(if (null? l1) acc
	(cons (cons (car l1) (* -1 (car l1))) (add-stream (cdr l1) (cons (car l1) (* -1 (car l1)))) )))

(define (int n k)
 (if (> n k) '()
	(cons n (int (+ n 1) k))))

(define x (int 1 14))
(add-stream  x '())