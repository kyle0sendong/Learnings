function newton_i()
  fx = '-x^3 - cos(x)';
  p0 = 10;
  TOL = 10^-5;
  MAX_ITERATION = 999;
  newton(fx, p0, TOL, MAX_ITERATION);
endfunction
