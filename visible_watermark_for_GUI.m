function picture = visible_watermark_for_GUI(cover, watermark, option)
picture_cover = load_pic(cover);
picture_mark = load_pic(watermark);
picture_marked = visible_watermark(picture_cover, picture_mark, option);
picture = 'cache/marked.jpg'
imwrite(picture_marked, picture);
end