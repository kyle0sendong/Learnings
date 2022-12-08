function [l, u] = lu(a)
    size_matrix = size(a);
    n = size_matrix(1);
    l = zeros(n);
    u = zeros(n);

    if a(1,1) == 0
        printf('Factorization impossible');
        return;
    endif

    if size_matrix(1) != size_matrix(2)
        printf('Not a square matrix');
        return;
    endif

    for k = 1:n(1)
        u(k,k) = a(k,k);

        for i = (k+1):n(1)
            l(i,k) = a(i,k)/u(k,k);
            u(k,i) = a(k,i);
        endfor

        for i = (k+1):n(1)
            for j = (k+1):n(1)
                a(i,j) = a(i,j) - (l(i,k) * u(k,j));
            endfor
        endfor
    endfor

    for i = 1:n(1)
        for j = 1:i
            if i == j
                l(i,j) = 1;
            endif
        endfor
    endfor

endfunction
