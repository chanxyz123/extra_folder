(define (stream-of-streams int naturals)
	(cons
		(map
			(lambda (x) (* (stream-of-streams naturals) x))
			int)
		(stream-of-streams int (stream naturals))))

(define (int-from n k)
 (if (> n k) '()
	(cons n (int-from (+ n 1) k))))

(define int
	(int-from 1 10))
(define naturals
	(int-from 1 10))

(define (stream-ref s n)
	(cond ((= n 0) (stream-of-streams s))
		(else (stream-ref (stream-of-streams s) (- n 1)))))

(stream-ref (stream-ref (stream-of-streams int naturals) 1) 2)