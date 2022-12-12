function p = fixedpoint(gx, p0, TOL, MAX_ITERATION)
  eval(['g = @(x) (' gx ');']);

  #Step 1
  i = 1;
  while i <= MAX_ITERATION
      p = g(p0); #compute p1

      printf('x%d = %.4f\n',i,p) #print solutions
      if abs(p-p0)<TOL
        break
      endif

      i++;
      p0 = p;
  endwhile

  if i >= MAX_ITERATION
  printf('Fixed point method failed after %d iterations\n', MAX_ITERATION-1);
  endif
endfunction
