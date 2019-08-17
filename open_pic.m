function picture_path = open_pic(picture_path)
disp("[Matlab function] open_pic");
picture = importdata(picture_path);
picture_path = 'C:/myFiles/python/pymatlab/cache/000.jpg'
imwrite(picture, picture_path);
%image(picture);
end