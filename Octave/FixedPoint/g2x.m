function g2x()
  g2 = '((x + 3 - x^4) / 2)^1/2';
  p0 = 1;
  TOL = 10^-7;
  MAX_ITERATION = 999;
  fixedpoint(g2, p0, TOL, MAX_ITERATION);
endfunction
