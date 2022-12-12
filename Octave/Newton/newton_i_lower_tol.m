# This function uses the newton()
# Does not accept user input

function newton_i_lower_tol()
  fx = '-x^3 - cos(x)';
  p0 = 10;
  TOL = 10^-8;
  MAX_ITERATION = 50;

  printf('\nf(x): %s\n', fx);
  printf('p0: %d\n', p0);
  printf('Tolerance: %.8f\n', TOL);
  printf('Max Iteration: %d\n\n', MAX_ITERATION);

  newton(fx, p0, TOL, MAX_ITERATION);

endfunction
