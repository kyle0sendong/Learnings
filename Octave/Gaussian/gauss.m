function gauss(A)

    [m,n] = size(A); # get size of matrix

    if n ~= m + 1 # check if no solution exists
        disp('No solution exists');
        return;
    endif

    # Gaussian Elimination
    for k = 1:n-1
        for i = k+1:m
            factor = A(i,k) / A(k,k);
            for j = k+1:n
                A(i,j) = A(i,j) - factor*A(k,j);
            endfor
            A(i,k) = 0;

            if A(k,k) == 0
                disp("No solution exists");
                return;
            endif
        endfor
    endfor

    # Backward Substitution
    x = zeros(m,1);
    for i = m:-1:1
        sum = 0;
        for j = i+1:m
            sum = sum + A(i,j)*x(j);
        endfor
        x(i) = (A(i,n)-sum)/A(i,i);
    endfor

    # Print solution
    for i=1:n-1
        printf('x%d = %d\n',i,x(i));
    endfor

endfunction
