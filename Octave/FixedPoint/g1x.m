function g1x()
  g1 = '(3*x^4 + 2*x^2+3)/(4*x^3+4*x-1)';
  p0 = 1;
  TOL = 10^-7;
  MAX_ITERATION = 999;
  fixedpoint(g1, p0, TOL, MAX_ITERATION);
endfunction
