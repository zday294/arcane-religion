clean:
	rm arc.o arclib.so car-app-c

car: arc.c compute-arcane-religion.c
	gcc -Wall -Wextra -o car-app-c compute-arcane-religion.c arc.c

shared: arc.o
	gcc arc.o -shared -o arclib.so

base: arc.c
	gcc -c -fPIC arc.c -o arc.o