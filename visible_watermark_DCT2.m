function picture = visible_watermark_DCT2(cover, watermark)
watermark_size = size(watermark);
block_size = 8;
for a = 1:(watermark_size/block_size)
    for b = 1:(watermark_size/block_size)
        watermark_block = watermark((a-1) * block_size + 1:a * block_size, (b-1) * block_size + 1:b * block_size);
        watermark_block = dct2(watermark_block);
        block = cover((a-1) * block_size + 1:a * block_size, (b-1) * block_size + 1:b * block_size);
        block = dct2(block);
        for i = 1:block_size
            for j = 1:block_size
                block(i,j) = 0.9 * block(i,j) + 0.5 * watermark_block(i,j) * 255;
            end
        end
        block = idct2(block);
        cover((a-1) * block_size + 1:a * block_size, (b-1) * block_size + 1:b * block_size) = block;
    end
end
picture = cover;
end