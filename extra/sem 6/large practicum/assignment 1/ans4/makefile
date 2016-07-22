obj = main.o factorial.o hello.o
hello : $(obj)
		g++ -o hello $(obj)

main.o : main.cpp functions.h

hello.o : hello.cpp functions.h

factorial.o : factorial.cpp functions.h