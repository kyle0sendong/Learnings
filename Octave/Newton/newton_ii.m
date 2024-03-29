function newton_ii()
  fx = 'x^2 - 6';
  p0 = 10;
  TOL = 10^-5;
  MAX_ITERATION = 999;

  printf('\nf(x): %s\n', fx);
  printf('p0: %d\n', p0);
  printf('Tolerance: %.5f\n', TOL);
  printf('Max Iteration: %d\n\n', MAX_ITERATION);

  newton(fx, p0, TOL, MAX_ITERATION);

  p0 = -10;
  TOL = 10^-5;
  MAX_ITERATION = 999;

  printf('\nf(x): %s\n', fx);
  printf('p0: %d\n', p0);
  printf('Tolerance: %.5f\n', TOL);
  printf('Max Iteration: %d\n\n', MAX_ITERATION);

  newton(fx, p0, TOL, MAX_ITERATION);

endfunction

