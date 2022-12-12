# This function uses g1(x) = '(3 + x - 2*(x^2))^(1/4)' and uses the fixedpoint function.
# This function uses all the given initial values for the p0 and tolerance
# This does not accept user input as it was not stated in the requirements.

function g1x()
  g = '(3 + x - 2*(x^2))^(1/4)';
  p0 = 1;
  TOL = 10^-7;
  MAX_ITERATION = 10;

  printf('\ng(x): %s\n', g);
  printf('p0: %d\n', p0);
  printf('Tolerance: %.7f\n', TOL);
  printf('Max Iteration: %d\n\n', MAX_ITERATION);

  fixedpoint(g, p0, TOL, MAX_ITERATION);

endfunction
