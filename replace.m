fid = fopen('train2.txt');  
fid1 = fopen('Hasan_train.txt','w');

data = fscanf(fid, '%c');

for i=2:length(data)-1
    if data(i)=='1' && data(i+1)=='5' && data(i+2)=='\'
        data(i)=' ';
    end
    fprintf(fid1,data(i));
end
    fprintf(fid1,data(i+1));


fclose(fid);
fclose(fid1);

