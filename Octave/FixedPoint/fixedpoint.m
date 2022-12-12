# Construct an Octave function for the fixed-point iteration

# This fixedpoint iteration accepts function of x, initial approximation p0, tolerance, and max iteration.
# This also returns p. It follows the algorithm given from the class powerpoint.

function p = fixedpoint(fx, p0, TOL, MAX_ITERATION)
  eval(['f = @(x) (' fx ');']);

  # Step 1
  i = 1;

  #Step 2
  while i <= MAX_ITERATION

    #Step 3 Compute pi
    p = f(p0);

    printf('x%d = %.6f\n', i, p) #print solutions for observations on convergence.

    # Step 4, check if procedure is succesful
    if abs(p-p0)<TOL
      break;
    endif

    # Step 5. update iterator for the while loop
    i++;

    # Step 6. Update p0.
    p0 = p;
  endwhile

  #Step 7. If approximation not found in the given iterations
  if i > MAX_ITERATION
    printf('Fixed point method failed after %d iterations\n', MAX_ITERATION);
  endif

endfunction
