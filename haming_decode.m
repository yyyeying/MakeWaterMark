function source = haming_decode(H, num_zero)
    source = [];
    %H为长度为7的序列
    h_size = size(H);
    h_size = h_size(2);
    groups = h_size/7;
    for index = 1:groups
        this_group = H((index-1)*7+1:index*7);
        S1=xor(this_group(1),xor(this_group(2),xor(this_group(3),this_group(5))));
        S2=xor(this_group(1),xor(this_group(2),xor(this_group(4),this_group(6))));
        S3=xor(this_group(1),xor(this_group(3),xor(this_group(4),this_group(7))));

        judge= 4*S1 + 2*S2 + S3;

        switch judge
            case 1
                this_group(7)=mod(this_group(7)+1,2);
            case 2
                this_group(6)=mod(this_group(6)+1,2);
            case 3
                this_group(4)=mod(this_group(4)+1,2);
            case 4
                this_group(5)=mod(this_group(5)+1,2);
            case 5
                this_group(3)=mod(this_group(3)+1,2);
            case 6
                this_group(2)=mod(this_group(2)+1,2);
            case 7
                this_group(1)=mod(this_group(1)+1,2);
        end
        source = [source, this_group(1:4)];
    end
    source_size = groups * 4;
    source = source(1:source_size-num_zero);
end



