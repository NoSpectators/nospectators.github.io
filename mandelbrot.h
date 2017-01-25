#include "complex.h"
#ifndef _MANDELBROT_H
#define _MANDELBROT_H

complex_t mandelbrot_simp ( complex_t c ); 
complex_t mandelbrot ( unsigned iterations, complex_t c );
complex_t complex_from_coord ( double x, double y );

#endif
