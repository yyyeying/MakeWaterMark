function path = robust_QIM_embed_for_GUI(cover_file, watermark)
disp('[Matlab function]robust_QIM_embed_for_GUI')
[picture, key_path] = watermark_spreading_QIM(cover_file, watermark, 128, 100)
path = [picture, ',', key_path]
end