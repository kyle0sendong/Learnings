function secant_num5()
    fx = '600*x^4 - 550*x^3 + 200*x^2 - 20*x - 1';
    p0 = 0.4;
    p1 = 0.8;
    TOL = 10^-8;
    MAX_ITERATION = 999;

    printf('\nf(x): %s\n', fx);
    printf('p0: %d\n', p0);
    printf('p1: %d\n', p1);
    printf('Tolerance: %.7f\n', TOL);
    printf('Max Iteration: %d\n\n', MAX_ITERATION);

    secant(fx, p0, p1, TOL, MAX_ITERATION);

endfunction
