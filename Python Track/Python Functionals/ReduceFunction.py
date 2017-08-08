def product(fracs):
    
    t = reduce(lambda f1, f2 : Fraction(f1.numerator * f2.numerator, f1.denominator * f2.denominator), fracs)
    return t.numerator, t.denominator