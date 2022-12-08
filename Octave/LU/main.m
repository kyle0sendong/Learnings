function main()
	output_precision(3)
	matrix = [2,-1,1; 3,3,9; 3,3,5]
	#matrix = [1,-1,5; -5,2,3; 3,3,2];
	#matrix = [1,2,4,1; 2,8,6,4; 3,10,8,8; 4,12,10,6];
	size_matrix = size(matrix);

	[l, u] = lu(size_matrix, matrix);
    printf('A = \n');
    disp(matrix);
	printf('L = \n');
    disp(l);
    printf('U = \n');
    disp(u);

	[l, u] = lu_1(size_matrix, matrix);
	printf('A = \n');
    disp(matrix);
	printf('L = \n');
    disp(l);
    printf('U = \n');
    disp(u);

endfunction