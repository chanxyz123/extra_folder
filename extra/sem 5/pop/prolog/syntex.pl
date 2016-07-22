weather(phoenix,summer,hot).
weather(la,summer,warm).
weather(phoenix,winter,warm).

warmer(C1,C2):-
	weather(C1,summer,hot),
	weather(C2,summer,warm),
	write(C1),write(' is warmer than '),write(C2),nl.