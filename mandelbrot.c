#include "mandelbrot.h"
#include "complex.h"

static const double max_radius = 1000.0;
static const unsigned max_iterations = 15;
static const complex_t max_size = { 1000.0, 1000.0 };

complex_t complex_from_coord (double x, double y) { 

    complex_t ret;
    ret.real = x;
    ret.imag = y;
    return ret;
}

complex_t mandelbrot_simp (complex_t c) { 

    return mandelbrot(15, c);
}

complex_t mandelbrot (unsigned iterations, complex_t c) { 

    if ( iterations == 0)
        return c;
    
    complex_t t = mandelbrot(iterations - 1, c);
    
    if (abs_complex(t).real > max_radius)
        return max_size;
    
    return add_complex(multiply_complex(t, t), c);
}
