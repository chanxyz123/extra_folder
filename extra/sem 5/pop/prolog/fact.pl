likes(dan,sally).
likes(sally,dan).
likes(joshy,josh).

dating(X,Y):-
	likes(X,Y),
	likes(Y,X).