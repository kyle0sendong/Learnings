function bisection_num5()
    fx = '600*x^4 - 550*x^3 + 200*x^2 - 20*x - 1';
    a = 0.2;
    b = 0.8;
    TOL = 10^-8;
    MAX_ITERATION = 999;

    printf('\nf(x): %s\n', fx);
    printf('Tolerance: %.7f\n', TOL);
    printf('Max Iteration: %d\n\n', MAX_ITERATION);
    printf('Interval a: %d\n', a);
    printf('Interval b: %d\n', b);

    bisection(fx, a, b, TOL, MAX_ITERATION);

endfunction
