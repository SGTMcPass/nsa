### How do I use inherited templates in the input file?

 ;
} ;

template < typename U > class Ca : public B<U> {
    public:
        Ca() : ca(4) {}
        U run_Ca() {
            return ca ;
        }
        U ca ;
} ;

// Trick does not currently write out the %template statement for specifically inherited template
#ifdef SWIG
%template(Bshort) B<short> ;
#endif

class Cb : public B<short> {
    public:
        Cb() : cb(5) {}
        double run_Cb() {
            return cb ;
        }
        double cb ;
} ;

// Trick does not create %template statements for lower level inherited classes.  B<float>
// is created by Cb<float>
#ifdef SWIG
%template(Bfloat) B<float> ;
#endif

class D {
    public:
        // Trick sees these template variables and auto generates
        // %template(Bdouble) B< double >
        // %template(Cafloat) Ca< float >
        B< double > my_b;
        Ca< float > my_ca;
        Cb my_cb;
} ;
```
