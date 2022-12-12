function newton_ii()
  fx = 'x^2 - 6';
  p0 = 10;
  TOL = 10^-5;
  MAX_ITERATION = 999;
  newton(fx, p0, TOL, MAX_ITERATION);

  p0 = -10;
  TOL = 10^-5;
  MAX_ITERATION = 999;
  newton(fx, p0, TOL, MAX_ITERATION);
endfunction

