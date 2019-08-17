function output = QIM_decode(value, level)
% Syntax: output = QIM_decode(value, level)
% 量化索引解调
    half_level = level / 2;
    abs_value = abs(value);
    levels = floor(abs_value / half_level);
    pixel = mod(abs_value, half_level);
    if pixel > (level/4)
        levels = levels + 1;
    end 
    if mod(levels, 2) == 1
        output = 1;
    else
        output = 0;
    end 
end