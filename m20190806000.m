watermark_file = 'watermark.txt';
cover_file = 'test2.jpg';
picture = jpeg_read(cover_file);
[picture, key_file] = jpeg_lbs(cover_file, watermark_file);
watermark = jpeg_lbs_extract(picture, key_file);