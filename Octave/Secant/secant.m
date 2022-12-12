function p =secant(fx, p0, p1, TOL, MAX_ITERATION)

    #https://stackoverflow.com/questions/64558908/how-to-read-function-from-keyboard-in-octave-and-use-it-later
    eval(['f = @(x) (' fx ');']);

	#Step 1
	q0 = f(p0);
	q1 = f(p1);
    p = 0;

    #Step 2
    i = 2;
    while(i <= MAX_ITERATION)

        #Step 3
        p = p1 - (q1*(p1 - p0)/(q1-q0));

        #Step 4
        if abs(p - p1) < TOL
            return;
        endif

        printf('Iteration %d: %f\n', i, p);

        #Step 5
        i++;

        #Step 6
        p0 = p1;
        p1 = p;
        q0 = q1;
        q1 = f(p1);

    endwhile

    #Step 7
    if i > MAX_ITERATION
        printf('p after %d iterations: %f\n', i-1, p);
        return;
    endif

endfunction
