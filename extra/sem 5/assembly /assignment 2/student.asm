%include "io.mac"

.DATA
msg1	db	"Enter the number of Students = ",0
msg2	db	"Enter the number of Subjects = ",0
msg3	db	"Enter the marks for each students = "

.UDATA
2darray	resw	100
array	resw	100
seracharr	resw	?.?
parray	resw	100
sarry  	resw	100
min		resw	10000
max		resw	100	
sum		resw	100
number1	resw	100
number2	resw	100
.CODE
		.STARTUP
		PutStr	msg1
		GetInt	CX
		PutStr	msg2
		GetInt	DX
		PutStr	msg3
input:
	mov AX,0
	mov ESI,0
	mov [sum],0
	loop1:	
			mov BX,0
			cmp CX,AX
			je	loop1_end
			loop2:
					cmp DX,BX
					je	loop2_end
					GetInt DI
					mov [2darray+ESI*4],DI
					add	[sum+ESI*4],DI
					inc ESI
					inc BX
					jmp	loop2
			loop2_end:
			jmp totalmarks
			mov [sum],0
			inc AX
			jmp	loop1
	loop1_end:


.EXIT
