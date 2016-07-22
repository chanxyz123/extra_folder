(define (attach-tag type-fac student)
  (cons type-fac student))

(define (type-tag datum)
  (if (pair? datum)
      (car datum)
      (error "Bad tagged datum -- TYPE-TAG" datum)))

(define (faculty datum)
  (if (pair? datum)
      (cdr datum)
      (error "Bad tagged datum -- CONTENTS" datum)))

(define (facA? z)
  (eq? (type-tag z) 'facA))

(define (facB? z)
  (eq? (type-tag z) 'facB))

(define (facC? z)
  (eq? (type-tag z) 'facB))

; ;Constructors
; (define (make-student-record rollNo name compile output viva)
; 	(list rollNo name compile output viva ))

(define (make-student-facA-record rollNo name compile output viva)
	(attach-tag 'facA
		(list rollNo name compile output viva)))

(define (make-student-facB-record rollNo name compile output viva)
	(attach-tag 'facB
		(list rollNo name compile output viva)))

(define (make-student-facC-record rollNo name compile output viva)
	(attach-tag 'facC
		(list rollNo name compile output viva)))

;Selectors

(define (get-name student)
	(caddr student))

(define (get-rollno student)
	(cadr student))

(define (get-compile-marks student)
	(cadddr student))


; faca 45 	sri 	3 			3 			(3 5)
; car  cadr caddr 	cadddr     caddddr  		cadddddr  

(define (get-output-marks student)
	(car (cdr (cdddr student))))

(define (get-viva-marks student)	
	(cdr (car (cdr (cdr(cdddr student))))))

(define (get-viva-strategy student)	
	(car (car (cdr (cdr(cdddr student))))))

(define (get-viva-strategy-multi x)
	(cond ((eq? x 'viva1) 0.7)
		((eq? x 'viva2) 0.8)
		((eq? x 'viva3) 0.9)))

;operation

(define (get-total-marks student)
	(+ (get-viva-marks student) (get-compile-marks student) (get-output-marks student)))

(define (calculate-normalized-score student-list)
	( map
		(lambda(x) 		
						(begin 
							(newline)
							(display (get-name x))
							(display  ": ")
							;NORMALIZED SCORE STARTS
							(display (+ 
								(* (get-viva-strategy-multi (get-viva-strategy x) ) 
									(get-viva-marks x)) 
							(get-compile-marks x) 
							(get-output-marks x)))
							;NORMALIZED SCORE ENDS
							; (display normal)
							; SIr Please Solve this issue
							; Unable to let normailesed score
							(newline)
							))
		student-list ))

(define (make-viva-strategy1 marks)
	(attach-tag 'viva1 marks) )

(define (make-viva-strategy2 marks)
	(attach-tag 'viva2 marks))

(define (make-viva-strategy3 marks)
	(attach-tag 'viva3 marks))

(define a (make-student-facA-record 45 'sriram 3 3 (make-viva-strategy3 5)))

(define b (make-student-facB-record 45 'gopal 3 3 (make-viva-strategy2 5)))

(define c (make-student-facC-record 45 'govind 3 3 (make-viva-strategy1 5)))

(calculate-normalized-score (list a b c)) 
