function main()
	clc
	clear

	output_precision(3)

	printf('Input Matrix in format [1,2,3; 4,5,6; 7,8,9]\n')
	matrix = input('Matrix A: ');
	[l, u] = lu(matrix);
	
    printf('A = \n');
    disp(matrix);
	printf('L = \n');
    disp(l);
    printf('U = \n');
    disp(u);

endfunction
