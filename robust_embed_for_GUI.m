function path = robust_embed_for_GUI(cover_file, watermark)
disp('[Matlab function]robust_embed_for_GUI')
[picture, key_path] = watermark_spreading(cover_file, watermark, 64)
path = [picture, ',', key_path]
end