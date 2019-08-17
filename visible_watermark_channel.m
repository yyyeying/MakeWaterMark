function picture = visible_watermark_channel(cover, watermark, option)
picture = cover;
[width, height] = size(watermark);
switch option
    case '1'
        for i = 1:width
            for j = 1:height
                if watermark(i,j) ~= watermark(1,1)
                    picture(i,j) = watermark(i,j);
                end
            end
        end
    case '2'
        for i = 1:width
            for j = 1:height
                if watermark(i,j) ~= watermark(1,1)
                    picture(i,j) = cover(i,j) + 150;
                end
            end
        end
        
    case '3'
        for i = 1:width
            for j = 1:height
                if watermark(i,j) ~= watermark(1,1)
                    picture(i,j) = (1.5) * cover(i,j);
                end
            end
        end
end
end
        