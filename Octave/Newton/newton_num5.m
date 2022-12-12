function newton_num5()
    fx = '600*x^4 - 550*x^3 + 200*x^2 - 20*x - 1';
    p0 = 0.2;
    TOL = 10^-8;
    MAX_ITERATION = 999;

    printf('\nf(x): %s\n', fx);
    printf('p0: %d\n', p0);
    printf('Tolerance: %.7f\n', TOL);
    printf('Max Iteration: %d\n\n', MAX_ITERATION);

    newton(fx, p0, TOL, MAX_ITERATION);

endfunction
