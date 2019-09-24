fid = fopen('tt.txt');  
fid1 = fopen('tw.txt','w');

data = fscanf(fid, '%c');

for i=1:length(data)-1
    if data(i)=='m' && data(i+1)==','
        data(i+1)=' ';
    end
    fprintf(fid1,data(i));
end
    fprintf(fid1,data(i+1));


fclose(fid);
fclose(fid1);

