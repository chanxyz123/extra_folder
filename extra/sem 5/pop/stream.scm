(define (proc x times pro)
	(define (P x times pro acc)
		(cond((= acc 0) (cons x (display (P (repeated x (+ acc 1) pro) times pro (+ acc 1)))))
			((= acc times)(repeated x acc pro))
			(else(P (repeated x (+ acc 1) pro) times pro (+ acc 1)))))
	(P x times pro 0))

(define (repeated x times pro)
	(cond((= times 1) (display (pro x)))
			(else(repeated (pro x) (- times 1) pro))))

(define (make-rep f)
	(lambda(x) (lambda (y) (proc x y f))))

(define (square x) (* x x))

(((make-rep square) 2) 3)