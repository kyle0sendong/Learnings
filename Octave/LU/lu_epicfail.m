function [l, u] = lu_1(nsize, a)
    n = nsize(1)
    l = zeros(nsize);
    u = zeros(nsize);

    if size(a, 1) != size(a, 2)
        printf('Not a square matrix');
        return;
    endif

    for i = 1:n
        for j = 1:i
            if i == j
                l(i,j) = 1;
                u(i,j) = 1;
            endif
        endfor
    endfor

    #Step 1
    if a(1,1) == 0
        printf('Factorization impossible\n');
        return;
    endif

    #Step 2
    for j = 2:n
        u(1,j) = a(1,j) / l(1,1);
        l(j,1) = a(j,1) / u(1,1);
    endfor

    #Step 3
    for i = 2:(n-1)

        #Step 4
        sum1 = 0;
        for k = 1:(i-1)
            sum1 += l(i,k) * u(k,i);
        endfor

        l(i,i), u(i,i) = a(i,i) - sum1;
        if l(i,i) == 0 || u(i,i) == 0
            printf('Factorization Impossible\n');
            return;
        endif

        #Step 5
        sum1 = 0;
        sum2 = 0;
        for j = (i+1):n
            for k = 1:(i-1)
                sum1 += l(i,k) * u(k,j);
                sum2 += l(j,k) * u(k,i);
            endfor
            u(i,j) = (1/l(i,i)) * (a(i,j) - sum1);
            l(j,i) = (1/u(i,i)) * (a(j,i) - sum2);
        endfor
    endfor

    #Step 6
    sum1 = 0;
    for k = 1:(n-1)
        sum1 += l(n,k) * u(k,n);
    endfor

    l(n,n), u(n,n) = a(n,n) - sum1;

    for i = 1:n
        for j = 1:i
            if i == j
                l(i,j) = 1;
            endif
        endfor
    endfor

endfunction
