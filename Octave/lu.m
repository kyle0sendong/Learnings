function [l, u] = lu(n, a)
    l = zeros(n);
    u = zeros(n);

    #Step 1
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
        printf('Factorization impossible');
        return;
    endif

    if size(a, 1) != size(a, 2)
        printf('Not a square matrix');
        return;
    endif

    #step 2
    for j = 2:n
        u(1,j) = a(1,j)/l(1,1);
        l(j,1) = a(j,1)/u(1,1);
    endfor

    #step 3
    for i = 2:n-1
        #step 4
        sum = 0;
        
        for k = 1:i-1
            sum +=  (l(i,k) * u(k,i));
        endfor

        l(i,i) = a(i,i) - sum;
        u(i,i) = a(i,i) - sum;

        if l(i,i) == 0 || u(i,i) == 0
            printf('Factorization Impossible');
            return;
        endif
        
        sum1 = 0;
        sum2 = 0;
        for j = i+1:n
            #ith row of u
            for k = 1:i-1;
                sum1 += l(i,k) * u(k,j);
                sum2 += l(j,k) * u(k,i);
            endfor
            u(i,j) = (1/l(i,i)) * (a(i,j) - sum1);
            l(j,i) = (1/u(i,i)) * (a(j,i) - sum2);
        endfor
    endfor

    disp(a);
    printf('\n');
    disp(u);
    printf('\n');
    disp(l);

endfunction


