;chandra jeet nagar	
;B13115
;cse
%include "io.mac"

.DATA
student db "Enter the number of students",10,0
subject db "Enter the number of subjects",10,0
Srch db "Enter the total marks to be searched ",10,0
max_size EQU 100

.UDATA
array resw max_size
sum resw max_size
per resw max_size
min resw max_size
max resw max_size

.CODE
	.STARTUP
	call input
	call total_marks
	call computing_per
	call Max_Min
	call Inertion_Sort
	;call Binary_search
done:
	.EXIT

input:
	PutStr student
	GetInt CX
	PutStr subject
	GetInt DX
	mov BX,CX
	sub ESI,ESI
	loop1:
		sub DI,DI
		loop2:
			cmp DX,DI
			je loop2_end 
			GetInt AX
			mov [array+ESI*4],AX
			inc ESI
			inc DI
			jmp loop2
		loop2_end:		
	loop loop1
	ret	
display:
	ret

total_marks:
	sub EDI,EDI
	sub ESI,ESI
	loop3:
		cmp EBX,EDI
		je loop3_end
		sub BP,BP
		sub CX,CX
		loop4:
			cmp DX,BP
			je loop4_end 
			mov AX,[array+ESI*4]
			inc ESI
			inc BP
			add CX,AX
			jmp loop4
		loop4_end:
		mov [sum + EDI*4],CX
		inc EDI
		jmp loop3
	loop3_end:
	ret

computing_per:
	mov CX ,BX
	sub ESI,ESI
	mov BP,100
	mov AX,DX
	mul BP
	mov BP,AX
	loop5:
		mov AX,[sum	+ESI*4]
		div BP
		mov [per+ ESI*4],AX
	ret

Max_Min:
	sub EDI,EDI
	sub ESI,ESI
	loop6:
		cmp EBX,EDI
		je loop6_end
		sub BP,BP
		sub CX,CX
		loop7:
			cmp DX,BP
			je loop7_end 
			mov AX,[array+ESI*4]
			inc ESI
			cmp BP,AX
			jl changmin
			changmin:
				mov BP,AX
			cmp AX,CX
			jg changmax
			changmax:
				mov CX,AX	
			jmp loop7
		loop7_end:
		mov [min +EDI*4],BP
		mov [max + EDI*4],CX
		inc EDI
		jmp loop6
	loop6_end:
	ret	

Inertion_Sort:
 ;to be performed on sum array.
	mov CX ,BX
	mov ESI,1
	loop8:
		mov AX,[sum	+ESI*4]
		mov EDI,ESI
		dec EDI
		while_loop:
			cmp AX,[sum + EDI*4]
			jge exit_while_loop
			mov  BP,[sum + EDI*4]
			mov [sum + EDI*4 + 4],BP
			dec EDI
			cmp EDI,0
			jge while_loop
		exit_while_loop:
		mov [sum + EDI*4 + 4],AX
	loop loop8	
	ret	

;Binary_search:
;	PutStr Srch
;	GetInt SI
;		mov BP,0
;		mov CX,BX
;		dec CX
;		while_loop:
;			cmp CX,BP
;			jl exit_while_loop
;			mov AX,CX
;			add AX,BP
;			div 2
;			mov DI,AX
;			cmp SI,[sum+EDI*4]
;			je search_done	
;			jg upper_half
;			lower_half:
;			
;			mid:
;				ret AX
;			cmp SI,[sum+EDI*4]
;				jl lessmid
;			lessmid:	
;				mov CX ,AX
;				dec CX
;			mov BP,AX
;			inc BP	
;