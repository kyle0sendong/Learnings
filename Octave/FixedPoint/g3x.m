function g3x()
  g3 = '((x+3) / (x^2+2))^1/2';
  p0 = 1;
  TOL = 10^-7;
  MAX_ITERATION = 999;

  fixedpoint(g3, p0, TOL, MAX_ITERATION);s
endfunction
