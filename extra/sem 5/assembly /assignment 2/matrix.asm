%include "io.mac"

.DATA
msg1	db	"Enter the number of Rows for matrix 1= ",0
msg2	db	"Enter the number of Columns for matrix 1= ",0
msg1	db	"Enter the number of Rows for matrix 2= ",0
msg2	db	"Enter the number of Columns for matrix 2= ",0

.UDATA
matrix1	db	dup("?") dup("?")
matrix2	db	dup("?") dup("?")
addmatrix	db	dup("?") dup("?")
array	db	dup("?")
seracharr	db	?.?


.CODE
		.STARTUP
			PutStr	msg1
			GetInt	CX
			PutStr	msg2
			GetInt	DX
			PutStr	msg3
			mov AX,0
input:
		mov BX,0
		lea SI,matrix1
		lea SP,matrix2
		loop1:	
				cmp CX,AX
				je	loop1_end
				mov matrix1[SI][BX],AX
				mov matrix2[SP][BX],AX
				loop2:
						cmp DX,BX
						je	loop2_end
						GetInt DI
						mov matrix[SI][BX],DI
						GetInt DI
						mov matrix[SP][BX],DI
						inc BX
						jmp	loop2
				loop2_end:
				inc AX
				jmp	loop1
		loop1_end:


add:
		mov BX,0
		mov AX,0
		lea SI,matrix1
		lea SP,matrix2
		lea DI,addmatrix
		loop1:	
				cmp CX,AX
				je	loop1_end
				mov addmatrix[DI][BX],AX
				loop2:
						cmp DX,BX
						je	loop2_end
						mov sum,matrix1[SI][BX]
						add sum,matrix2[SP][BX]
						mov addmatrix[DI][BX],sum
						mov sum,0
						inc BX
						jmp	loop2
				loop2_end:
				inc AX
				jmp	loop1
		loop1_end:	
subtract:
		mov BX,0
		mov AX,0
		lea SI,matrix1
		lea SP,matrix2
		lea DI,addmatrix
		loop1:	
				cmp CX,AX
				je	loop1_end
				mov addmatrix[DI][BX],AX
				loop2:
						cmp DX,BX
						je	loop2_end
						mov sum,matrix1[SI][BX]
						sub sum,matrix2[SP][BX]
						mov addmatrix[DI][BX],sum
						mov sum,0
						inc BX
						jmp	loop2
				loop2_end:
				inc AX
				jmp	loop1
		loop1_end:	


