function g4x()
  g4 = '(3*(x^4) + 2*(x^2) + 3) / ((4*(x^3)) + 4*x - 1)';
  p0 = 1;
  TOL = 10^-7;
  MAX_ITERATION = 15;

  fixedpoint(g4, p0, TOL, MAX_ITERATION);
endfunction
