#output, returns p
function p = newton(fx, p0, TOL, MAX_ITERATION)
  eval(['f = @(x) (' fx ');']);

  #Taking derivatives algo from https://wiki.octave.org/Symbolic_package
  pkg load symbolic;
  syms x;

  f_prime = diff(fx, x);
  f_prime = function_handle(f_prime);

  i=1;
  while i <= MAX_ITERATION

    p = p0 - (f(p0) / f_prime(p0));

    if abs(p-p0) < TOL
      break;
    endif

    printf('p%d = %.4f\n', i, p);

    i++;
    p0 = p;

  endwhile

endfunction
