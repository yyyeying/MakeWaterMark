picture_file = '10.jpg';
key_file = 'key10.txt';
watermark = 'msg.txt';
watermark_file = fopen(watermark, 'r');
watermark_text = fread(watermark_file);
watermark_size = size(watermark_text);
watermark_size = watermark_size(1);
bit_error_rate_list = [];
byte_error_rate_list = [];
r_list = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45];
for index = r_list
    bit_error_num = 0;
    byte_error_num = 0;
    watermark_extract = watermark_spreading_extract(0, picture_file, key_file, index);
    watermark_extract = double(watermark_extract);
    for i = 1:watermark_size
        if watermark_extract(i) ~= watermark_text(i)
            byte_error_num = byte_error_num + 1;
        end
        for j = 1:8
            %9-j
            % bitget(watermark_text(i), 9-j)
            bitget(watermark_extract(i), 9-j);
            if bitget(watermark_extract(i), 9-j) ~= bitget(watermark_text(i), 9-j)
                bit_error_num = bit_error_num + 1;
            end
        end
    end
    %bit_error_num
    %byte_error_num
    bit_error_rate = bit_error_num/(watermark_size*8);
    bit_error_rate_list = [bit_error_rate_list, bit_error_rate];
    byte_error_rate = byte_error_num/watermark_size;
    byte_error_rate_list = [byte_error_rate_list, byte_error_rate];
    fclose(watermark_file);
end
subplot(2,1,1)
bit_error_rate_list
plot(r_list, bit_error_rate_list)
%plot(quality_list, bit_error_rate_list)
title('Bit Error Rate')
subplot(2,1,2)
byte_error_rate_list
plot(r_list, byte_error_rate_list)
%plot(quality_list, byte_error_rate_list)
title('Byte Error Rate')
fclose('all');