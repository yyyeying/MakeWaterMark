function picture = visible_watermark(cover, watermark, option)
[mark_width, mark_height, cover_channel] = size(cover);
disp(cover_channel)
[mark_width,  mark_height, mark_channel] = size(watermark);
disp(mark_channel)
picture = cover;
if cover_channel == 3
    disp('cover_channel = 1')
    if mark_channel == 3
        disp('mark_channel = 3')
        picture(:,:,1) = visible_watermark_channel(cover(:,:,1), watermark(:,:,1), option);
        picture(:,:,2) = visible_watermark_channel(cover(:,:,2), watermark(:,:,2), option);
        picture(:,:,3) = visible_watermark_channel(cover(:,:,3), watermark(:,:,3), option);
    elseif mark_channel == 1
        picture(:,:,1) = visible_watermark_channel(cover(:,:,1), watermark, option);
        picture(:,:,2) = visible_watermark_channel(cover(:,:,2), watermark, option);
        picture(:,:,3) = visible_watermark_channel(cover(:,:,3), watermark, option);
    end
else
    picture = visible_watermark_channel(cover, watermark, option)
end