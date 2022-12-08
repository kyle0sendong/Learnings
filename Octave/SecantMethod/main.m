function main()
	clear;
	clc;

	fx = input('f(x) = ', 's');
	p0 = input('P0 = ');
    p1 = input('P1 = ');
	TOL = input('Tolerance = ');
	MAX_ITERATION = input('Max Iteration = ');

	[p, i] = secant(fx, p0, p1, TOL, MAX_ITERATION);

	#Step 7
	printf('Root: %f\n', p);
	printf('Found after %d iterations.\n', i)

endfunction
