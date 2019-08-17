cover = 'lena.bmp';
watermark = 'watermark.txt';
watermark_file = fopen(watermark, 'r');
watermark_text = fread(watermark_file);
watermark_size = size(watermark_text);
watermark_size = watermark_size(1);
%watermark_size
bit_error_rate_list = [];
byte_error_rate_list = [];
spread_times_list = [];
radius_list = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65];
for k = 1:100
    bl = [];
    quality = k;
    spread_times =  10;
    spread_times_list = [spread_times_list, spread_times];
    radius = k;
    for m = 1:20
        [picture, key] = watermark_spreading_QIM(cover, watermark, spread_times ,quality);
        watermark_extract_QIM = watermark_spreading_QIM_extract(picture, key);
        %watermark_extract_no_cover = watermark_spreading_QIM_extract(0, picture, key, k);
        %watermark_extract_with_cover = watermark_spreading_extract(cover, picture, key, 3);
        bit_error_num = 0;
        byte_error_num = 0;
        watermark_extract = double(watermark_extract_QIM);
        %watermark_extract = double(watermark_extract_no_cover);
        %watermark_extract = double(watermark_extract_with_cover);
        % watermark_extract = watermark_extract_with_cover;
        for i = 1:watermark_size
            watermark_extract(i);
            if watermark_extract(i) ~= watermark_text(i)
                byte_error_num = byte_error_num + 1;
            end
            for j = 1:8
                if bitget(watermark_extract(i), 9-j) ~= bitget(watermark_text(i), 9-j)
                    bit_error_num = bit_error_num + 1;
                end
            end
        end
        be = bit_error_num/(watermark_size*8);
        bl = [bl, be];
        %fclose(watermark_file);
    end
    %bit_error_num
    %byte_error_num
    bit_error_rate = mean(bl);
    bit_error_rate_list = [bit_error_rate_list, bit_error_rate];
    %byte_error_rate = byte_error_num/watermark_size;
    %byte_error_rate_list = [byte_error_rate_list, byte_error_rate];
    
end
%spread_times_list 
%bit_error_rate_list = sprintf('%2.2f%%', bit_error_rate_list*100)
%byte_error_rate_list = sprintf('%2.2f%%', byte_error_rate_list*100)
quality_list = [1:100];
%subplot(2,1,1)
%bit_error_rate_list
%plot(spread_times_list, bit_error_rate_list)
plot(quality_list, bit_error_rate_list)
%plot(radius_list, bit_error_rate_list)
%title('Bit Error Rate')
%subplot(2,1,2)
%byte_error_rate_list
%plot(spread_times_list, byte_error_rate_list)
%plot(quality_list, byte_error_rate_list)
%title('Byte Error Rate')
fclose('all');
