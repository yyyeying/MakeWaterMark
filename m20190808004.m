cover = '(1).tiff';
watermark = 'msg.txt';
watermark_file = fopen(watermark, 'r');
watermark_text = fscanf(watermark_file,'%s');
spread_times = 50;
[picture, key] = watermark_spreading_QIM(cover, watermark, spread_times, 40);
watermark_extract_no_cover = watermark_spreading_QIM_extract(picture, key);
% picture = 'spreading_QIM.jpg'
% picture = 'spreading_QIM.bmp'
% key = 'key.txt'
watermark_extract = watermark_spreading_QIM_extract(picture, key);
watermark = 'watermark.txt';
watermark_file = fopen(watermark, 'r');
watermark_text = fread(watermark_file);
watermark_size = size(watermark_text);
watermark_size = watermark_size(1);
bit_error_num = 0;
byte_error_num = 0;
watermark_extract = double(watermark_extract);
for i = 1:watermark_size
    if watermark_extract(i) ~= watermark_text(i)
        byte_error_num = byte_error_num + 1;
    end
    for j = 1:8
        if bitget(watermark_extract(i), 9-j) ~= bitget(watermark_text(i), 9-j)
            bit_error_num = bit_error_num + 1;
        end
    end
end
bit_error_rate = bit_error_num/(watermark_size*8);
byte_error_rate = byte_error_num/watermark_size;
disp('Bit Error Rate');
sprintf('%2.2f%%', bit_error_rate*100)
disp('Byte Error Rate');
sprintf('%2.2f%%', byte_error_rate*100)