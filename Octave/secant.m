function secant(p0, p1)
    q0 = f(p0);
    q1 = f(p1);
    p = 0;

    MAX_ITERATION = 999;
    TOL = 10^-8;

    i = 2;
    while(i <= MAX_ITERATION)

        p = p1 - (q1*(p1 - p0)/(q1-q0));

        if abs(p - p1) < TOL
            printf('Root found: %f\n', p);
            printf('Iteration: %d\n', i)
            break;
        endif

        i++;

        p0 = p1;
        p1 = p;
        q0 = q1;
        q1 = f(p1);
        
    endwhile

    if i > MAX_ITERATION
        printf('p after %d iterations: %f\n', i-1, p)
    endif

endfunction

function y = f(x)
    y =  x^3 - x + 2;
endfunction
