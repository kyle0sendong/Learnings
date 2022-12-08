function main()
	clear;
	clc;

	fx = input('f(x) = ', 's');
	p0 = input('P0 = ');
    p1 = input('P1 = ');
	TOL = input('Tolerance = ');
	MAX_ITERATION = input('Max Iteration = ');

	secant(fx, p0, p1, TOL, MAX_ITERATION);

endfunction
