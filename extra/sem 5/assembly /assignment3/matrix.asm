;Author = chandra jeet nagar	
;Rolln = b13115
;Branch = CSE

%include "io.mac"

.DATA
msg1	db	"Enter the number of Rows for matrix 1= ",0
msg2	db	"Enter the number of Columns for matrix 1= ",0
msg3	db	" ",0

.UDATA
matrix1	resw	80
matrix2	resw	80
addmatrix 	resw	100
submatrix 	resw	100
mulmatrix 	resw	100


.CODE

input:
		PutStr	msg1
		GetInt	CX
		PutStr	msg2
		GetInt	DX
		mov AX,0
		mov ESI,0
		loop1:	
				mov BX,0
				cmp CX,AX
				je	loop1_end
				loop2:
						cmp DX,BX
						je loop2_end
						GetInt DI
						mov [matrix1+ESI*4],DI
						GetInt DI
						mov [matrix2+ESI*4],DI
						inc ESI
						inc BX
						jmp	loop2
				loop2_end:
				inc AX
				jmp	loop1
		loop1_end:
add:
		
		mov AX,0
		mov ESI,0
		loop3:	
				mov BX,0
				cmp CX,AX
				je	loop3_end
				loop4:
						cmp DX,BX
						je	loop4_end
						mov SP,[matrix1+ESI*4]
						add SP,[matrix2+ESI*4]
						mov [addmatrix+ESI*4],SP
						mov SP,0
						inc ESI
						inc BX
						jmp	loop4
				loop4_end:
				inc AX
				jmp	loop3
		loop3_end:


subtract:
		mov AX,0
		mov ESI,0
		loop5:	
				mov BX,0
				cmp CX,AX
				je	loop5_end
				;mov [submatrix+BX],AX
				loop6:
						cmp DX,BX
						je	loop6_end
						mov SP,[matrix1+ESI*4]
						sub SP,[matrix2+ESI*4]
						mov [submatrix+ESI*4],SP
						mov SP,0
						inc ESI
						inc BX
						jmp	loop6
				loop6_end:
				inc AX
				jmp	loop5
		loop5_end:




addprint:
		
		mov AX,0
		mov ESI,0
		loop7:
				mov BX,0
				cmp CX,AX
				je	loop7_end
				loop8:
						cmp DX,BX
						je	loop8_end
						PutInt [addmatrix+ESI*4]
						PutStr msg3
						inc ESI
						inc BX
						jmp	loop8
				loop8_end:
				nwln
				inc AX
				jmp	loop7
		loop7_end:	


subprint:
		
		mov AX,0
		mov ESI,0
		loop9:
				mov BX,0
				cmp CX,AX
				je	loop9_end
				loop10:
						cmp DX,BX
						je	loop10_end
						PutInt [submatrix+ESI*4]
						PutStr msg3
						inc ESI
						inc BX
						jmp	loop10
				loop10_end:
				nwln
				inc AX
				jmp	loop9
		loop9_end:	


multiplecation:
				mov BP,0
				mov ESI,0
				mov EAX,0
				loop11:
						mov BX,0
						loop12:
								mov DI,0
								cmp DX,BX
								je loop12_end
								loop13:
										cmp DX,DI
										je	loop13_end
										mov AX,[matrix1+ESI*4]
										mov SP,[matrix2+ESI*8]
										mul SP 				
										mov AH,0
										add BP,AX
										inc ESI
										inc DI
								loop13_end:
								mov [mulmatrix+EAX*4],BP
								inc EAX
								inc BX
						loop12_end:
				loop11_end:	



			.EXIT