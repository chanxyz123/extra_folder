;Test routine for GetPut.asm     test.asm 
;
;       Objective: find the sum of numbers 
;       Input: Requests n integers  from the user.
;       Output: Outputs the input number.
%include "io.mac"

.DATA
prompt_msg1  db   "Enter numbers to sum: ",0
prompt_msg2  db   " input the number : ",0
output_msg  db   "The sum is :",0
.UDATA 
number1   resd   1 
number2   resd   1

.CODE
      .STARTUP
      PutStr  prompt_msg1   ; print msg 
      GetInt CX             ; CX= numbers to be entered  
      PutStr  prompt_msg2   ; print msg
      sub BX,BX              ;BX = 0
      mov AX,BX               ;AX = 0
loop_begin:
      cmp CX,BX 
      je loop_end
      jne sum
sum: 
      GetInt DX               ;get value to DX
      inc BX
      add AX, DX              ;add them to AX
      jmp loop_begin 
loop_end:          
      PutStr  output_msg      ;print output msg
      PutInt  AX              ;print output sum
     nwln                     ;new line
done:
      .EXIT                   ;end of the code segment









