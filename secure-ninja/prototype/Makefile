PROJECT = bin/p_maths
OBJ     = developer/project_maths.o swh1/add.o swh2/subtract.o
KEYS    = developer/keys.h swh1/key.h swh2/key.h

C99     = gcc -std=c99
CFLAGS  = -Wall -pedantic -Werror


$(PROJECT) : $(OBJ)
	mkdir bin
	$(C99) $(CFLAGS) -o $(PROJECT) $(OBJ)

developer/project_maths.o : developer/project_maths.c developer/keys.h
	cd developer; $(C99) $(CFLAGS) -c project_maths.c

swh1/add.o : swh1/add.c swh1/add.h swh1/key.h
	cd swh1; $(C99) $(CFLAGS) -c add.c

swh2/subtract.o : swh2/subtract.c swh2/subtract.h swh1/key.h
	cd swh2; $(C99) $(CFLAGS) -c subtract.c

test:
	$(PROJECT) -i8 -a5 -s8
	$(PROJECT) -i8 -s5 -a-5

clean:
	rm $(PROJECT) $(OBJ)

reset:
	make clean
	rm $(KEYS)
	rmdir bin
