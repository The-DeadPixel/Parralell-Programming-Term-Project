CC = g++
DEBUG = -g
CFLAGS = -Wall -c $(DEBUG)
LFLAGS = -Wall $(DEBUG)
OBJS = main.o fDriver.o lexo.o StemExcep.o Stem.o
INCLUDE = -I.

all : $(OBJS)
	$(CC) $(OBJS) $(LFLAGS) $(INCLUDE) -o SearchSeq

main.o : main.cpp fDriver.cpp
	$(CC) main.cpp $(INCLUDE) $(CFLAGS)

fDriver.o : fDriver.cpp fDriver.h lexo.cpp StemExcep.cpp
	$(CC) fDriver.cpp $(INCLUDE) $(CFLAGS)

lexo.o : lexo.cpp lexo.h Stem.cpp
	$(CC) lexo.cpp $(INCLUDE) $(CFLAGS)

StemExcep.o: StemExcep.cpp StemExcep.h
	$(CC) StemExcep.cpp $(INCLUDE) $(CFLAGS)

Stem.o : Stem.cpp Stem.h
	$(CC) Stem.cpp $(INCLUDE) $(CFLAGS)

clean :
	-rm *.o SearchSeq

tar :
	tar cvf FinalProject.tar Makefile main.cpp fDriver.cpp fDriver.h lexo.cpp lexo.h Stem.cpp Stem.h StemExcep.cpp StemExcep.h
