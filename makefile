mandelbrot : main.o mandelbrot.o complex.o
	gcc -o mandelbrot main.o mandelbrot.o complex.o -lm

main.o : mandelbrot.h complex.h
	gcc -c main.c

mandelbrot.o : mandelbrot.h complex.h
	gcc -c mandelbrot.c

complex.o : mandelbrot.h complex.h
	gcc -c complex.c

clean: 
	rm *.o
