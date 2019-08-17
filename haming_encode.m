function [Hamcode,num_zero] = haming_encode(H)
%H为输入随机序列
Ham=[];

len = length(H); 
   
a = mod(len,4);
num_zero=0;

%不足4的倍数补0
if a ~= 0
    for i=1 : 4-a
        H(len+i)=0;
        num_zero=4-a;
    end
end
len_addzero = len + num_zero;
       
% 产生校验

for i=1 : len_addzero/4
    for j=1 : 4
        Ham(i,j)=H((i-1)*4+j);
    end
end



for i = 1:len_addzero/4
    value = Ham(i,1)*8 + Ham(i,2)*4 + Ham(i,3)*2 + Ham(i,4);
    switch value
    case 0
        Ham(i, 5) = 0;
        Ham(i, 6) = 0;
        Ham(i, 7) = 0;
    case 1
        Ham(i, 5) = 0;
        Ham(i, 6) = 1;
        Ham(i, 7) = 1;
    case 2
        Ham(i, 5) = 1;
        Ham(i, 6) = 0;
        Ham(i, 7) = 1;
    case 3
        Ham(i, 5) = 1;
        Ham(i, 6) = 1;
        Ham(i, 7) = 0;
    case 4
        Ham(i, 5) = 1;
        Ham(i, 6) = 1;
        Ham(i, 7) = 0;
    case 5
        Ham(i, 5) = 1;
        Ham(i, 6) = 0;
        Ham(i, 7) = 1;
    case 6
        Ham(i, 5) = 0;
        Ham(i, 6) = 1;
        Ham(i, 7) = 1;
    case 7
        Ham(i, 5) = 0;
        Ham(i, 6) = 0;
        Ham(i, 7) = 0;
    case 8
        Ham(i, 5) = 1;
        Ham(i, 6) = 1;
        Ham(i, 7) = 1;
    case 9
        Ham(i, 5) = 1;
        Ham(i, 6) = 0;
        Ham(i, 7) = 0;
    case 10
        Ham(i, 5) = 0;
        Ham(i, 6) = 1;
        Ham(i, 7) = 0;
    case 11
        Ham(i, 5) = 0;
        Ham(i, 6) = 0;
        Ham(i, 7) = 1;
    case 12
        Ham(i, 5) = 0;
        Ham(i, 6) = 0;
        Ham(i, 7) = 1;
    case 13
        Ham(i, 5) = 0;
        Ham(i, 6) = 1;
        Ham(i, 7) = 0;
    case 14
        Ham(i, 5) = 1;
        Ham(i, 6) = 0;
        Ham(i, 7) = 0;
    case 15
        Ham(i, 5) = 1;
        Ham(i, 6) = 1;
        Ham(i, 7) = 1;
    end
end
Ham;

Hamcode=Ham';
Hamcode=(Hamcode(:))';
end

    
    
    
    
            
        
