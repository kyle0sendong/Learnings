# Create an Octave program that follows the given algorithm for the bisection method. The
# output must display, for each iteration, the intervals being used, the computed midpoints,
# and the function values using the obtained midpoints.

#This program uses the pseudocode provided in the powerpoint

function p = bisection(fx, a, b, TOL, MAX_ITERATION)
  eval(['f = @(x) (' fx ');']);

  p = 0;
  i = 1;
  fa = f(a);

  # Outputs the required information
  printf('  Iteration\t  an \t\t bn\t\t pn\t\t f(pn)\n');

  #Step 2 + Step 4
  while abs(f(a)) > TOL

    #Step 2
    if i > MAX_ITERATION
      printf('Method failed to converge after %d iterations\n', i);
      return;
    endif

    #Step 3
    p =  a + (b-a)/2;
    fp = f(p);

    #Step 4
    if fp == 0 || (b-a)/2 < TOL
      return;
    endif

    #Step 5
    i++;

    #Step 6
    if fa * fp > 0
      a = p;
      fa = fp;
    else
      b = p;
    endif

    printf('\t%d\t %.6f\t %.6f\t %.6f\t %.6f \n', i, a, b, p, fp);
  endwhile

endfunction
