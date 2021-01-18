from skimage import io
img1=io.imread("netaji.jpg")
k=((len(img1)*len(img1[1]))/80000)**(.5)
r=int(len(img1)/(len(img1)/k))
c=int(len(img1[1])/(len(img1[1])/k))
f=open("ascii_art_potrairt_netaji.txt","w")
char_dense="@B8&WM#YXQO{}[]()I1i\|!pao;:,.   "
c_l=len(char_dense);s=0
for i in range(int(c/2),len(img1),c):
    for j in range(int(r/2),len(img1[i]),r):
       colour=(((img1[i][j][0])*0.3)+((img1[i][j][0])*0.59)+((img1[i][j][0])*0.11))
       f.write(char_dense[int(colour*c_l/256)]);f.write(char_dense[int(colour*c_l/256)]);s+=2
    f.write("\n")
f.close();print(s)