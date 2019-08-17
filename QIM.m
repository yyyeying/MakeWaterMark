function out = QIM(value, level, bit)
    % QIM: 将一个像素点的值value根据随机序列的一位bit进行量化索引调制
    % value: 原像素值
    % level: 量化步长
    % bit: 随机序列的相应位
    % 若level = 10, 末位0代表0，末位5代表1.
    abs_value = abs(value);
    half_level = level/2;
    i_value = floor(abs_value/half_level);
    if bit == 0
        if mod(i_value,2)==0
            out = i_value*half_level;
        else
            out = (i_value+1)*half_level;
        end
    else
        if mod(i_value,2)==1
            out = i_value*half_level;
        else
            out = (i_value+1)*half_level;
        end
    end
    if out == 0
        out = level;
    end
    if value<0
        out = -out;
    end
end