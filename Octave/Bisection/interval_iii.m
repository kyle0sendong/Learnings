# Construct separate codes that use your program 'bisection.m'
# for the bisection method to solve the above problem for each interval

# Driver code where interval_iii where interval a, b = [2, 3]

function interval_iii()
    fx = 'x^4 - (2*x^3) - (4*(x^2)) + 4*x + 4';
    a = 2;
    b = 3;
    TOL = 10^-7;
    MAX_ITERATION = 999;

    printf('\nf(x): %s\n', fx);
    printf('Tolerance: %.7f\n', TOL);
    printf('Max Iteration: %d\n\n', MAX_ITERATION);
    printf('Interval a: %d\n', a);
    printf('Interval b: %d\n', b);
    bisection(fx, a, b, TOL, MAX_ITERATION);

endfunction