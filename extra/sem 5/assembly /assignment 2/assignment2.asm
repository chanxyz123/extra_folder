;Test routine for GetPut.asm     test.asm 
;
;       Objective: find the sum of numbers 
;       Input: Requests n integers  from the user.
;       Output: Outputs the input number.
%include "io.mac"

.DATA
prompt_msg1  db   "Enter numbers to sum: ",0
prompt_msg2  db   " input the number : ",0
output_msg1  db   "Sum =",0
output_msg2  db   "Mean =",0
output_msg3   db   "Varience = ",0
.UDATA 
number1   resd   1 
number2   resd   1

.CODE
      .STARTUP
      PutStr  prompt_msg1   ; print msg 
      GetInt CX             ; CX= numbers to be entered  
      PutStr  prompt_msg2   ; print msg
      sub BX,BX              ;BX = 0
      mov SI,BX 
      mov DI,BX              ;AX = 0
loop_begin:
      sub AX,AX
      cmp CX,BX 
      je loop_end
      jne sum
sum: 
      GetInt DX               ;get value to DX
      inc BX
      add SI, DX              ;add them to AX
      mov AX,DX
      mul AX
      add DI,AX
      jmp loop_begin 
loop_end: 
      PutStr  output_msg1      ;print output msg
      PutInt  SI              ;print output sum
     nwln                     ;new line
     PutStr  output_msg2
     mov AX,SI
     div CL
     mov AH,0
     mov BX,AX
    PutInt  AX
    mul BX
    mov BX,AX
     nwln
     mov AX,DI
     div CL
     mov AH,0
     mov DX,AX
     sub DX,BX
     PutStr  output_msg3
     PutInt DX
     nwln
done:
      .EXIT                   ;end of the code segment







