cover = 'lena.bmp';
watermark = 'watermark.txt';
watermark_file = fopen(watermark, 'r');
watermark_text = fscanf(watermark_file,'%s');
[picture, key] = watermark_spreading_QIM(cover, watermark);
watermark_extract_no_cover = watermark_spreading_QIM_extract(picture, key);