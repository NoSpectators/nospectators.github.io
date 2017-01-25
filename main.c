#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

#include "complex.h"
#include "mandelbrot.h"

static const double inclusion_size = 100.0;

int main ( int argc, char *argv[] ) { 

    static const double start_x = -2.1, start_y = -1.2;
    static const double step_x = 0.032, step_y = 0.05;

    size_t row;
    for ( row = 0; row < 45; row++ ) { 
    
        size_t col;
        for ( col = 0; col < 80; col++ ){
        
            complex_t c = complex_from_coord(
                start_x + col*step_x,
                start_y + row*step_y
            );
            putchar( abs_complex(mandelbrot_simp(c)).real < inclusion_size ? '#' : ' ' );
        }
        putchar( '\n' ); 
    }

    return EXIT_SUCCESS;
}
