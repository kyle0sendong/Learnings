# Newton-Raphson method where it accepts fx, p0, tolerance and max iteration as a function parameters.
# This uses the symbolic package to take the derivatives of polynomials.

function p = newton(fx, p0, TOL, MAX_ITERATION)
  eval(['f = @(x) (' fx ');']);

  #Taking derivatives algo from https://wiki.octave.org/Symbolic_package
  pkg load symbolic;
  syms x;
  f_prime = diff(fx, x);
  f_prime = function_handle(f_prime);

  # Step 1.
  i=1;

  # Step 2. 
  while i <= MAX_ITERATION

    # Step 3. Taking the value of p using the formula.
    p = p0 - (f(p0) / f_prime(p0));

    # Step 4. Procedure was successful.
    if abs(p-p0) < TOL
      break;
    endif

    printf('p%d = %.6f\n', i, p); #Print P to check convergence for observations.

    #Step 5. Update iterator
    i++;

    #Step 6. Update p0
    p0 = p;

  endwhile

  #Step 7. If approximation not found in the given iterations
  if i > MAX_ITERATION
    printf('Fixed point method failed after %d iterations\n', MAX_ITERATION);
  endif

endfunction
