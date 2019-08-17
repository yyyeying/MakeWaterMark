function [picture, key_path] = watermark_spreading_QIM(cover, watermark, spread_times, quality)
%spread_times = 128;
QIM_step = 10;
watermark_file = fopen(watermark, 'r');
watermark_text = fread(watermark_file);
watermark_size = size(watermark_text);
watermark_size = watermark_size(1);
[false_random_list, x0, u0] = random_list(spread_times, 2, 5);
spreading_list = [];
new_random_list = [];
for i = 1:watermark_size
    for j = 1:8
        new_random_list = [new_random_list, false_random_list];
        for k = 1:spread_times
            spreading_list = [spreading_list, bitget(watermark_text(i), 9-j)];
        end
    end
end 
message_list = xor(new_random_list, spreading_list);
[message_list, num_zero] = haming_encode(message_list);
message_size = size(message_list);
message_size = message_size(2);
%message_size = watermark_size*8*spread_times;
cover_map = load_pic(cover);
[cover_width, cover_height, cover_channel] = size(cover_map);
x_ = fix(message_size/cover_width);
y_ = mod(message_size, cover_width);
y = fix((cover_width-y_)*rand);
x = fix((cover_height-x_)*rand);
col = 0;
row = y;
%disp('x')
%disp(x+col)
%disp('y')
%disp(row)
for i = 1:message_size
    cover_map(x+col, row) = QIM(cover_map(x+col, row), QIM_step, message_list(i));
    row = row + 1;
    if row == cover_width
        col = col+1;
        row = 1;
    end
end
%disp('x')
%disp(x+col)
%disp('y')
%disp(row)
position = [x, y, watermark_size, spread_times, x0, u0, QIM_step, message_size, num_zero];
key = num2str(position);
key_path = 'key.txt';
key_file = fopen(key_path, 'w');
fprintf(key_file, '%s', key);
picture = 'spreading_QIM.jpg';
imwrite(cover_map, picture, 'jpg', 'quality', quality);
% print(cover_map, 'djpeg', picture)
fclose(watermark_file)
end