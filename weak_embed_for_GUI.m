function path = weak_embed_for_GUI(cover_file, watermark)
[picture, key_path] = jpeg_lbs(cover_file, watermark)
path = [picture, ',', key_path]
end