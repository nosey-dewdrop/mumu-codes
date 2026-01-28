public interface Algebraic {

    Algebraic negate();
    Algebraic add(Algebraic other);
    Algebraic subtract(Algebraic other);
    Algebraic multiply(Algebraic other);

}

// an interface is to declare which functions subclasses should implement

/*
- polymorphisim
- common operations are declared. every algebraic object must do these four operations.
- returns are algebraic.
v + v = v
m + m = m
ltm + ltm = ltm 
*/
