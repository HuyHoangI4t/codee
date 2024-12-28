// dinh nghia 1 lớp hình chữ nhật có các phương thức tính diện tích, tính chu vi, xác định 1 điểm có nằm trong hình chữ nhật hay ko? Yêu cầu: nhập vào 1 hình chữ nhật, xuất ra  diện tích chu vi hình chữ nhật đó. Nhập vào 1 điểm, kiểm tra điểm đó có nằm trong hình chữ nhật hay ko
// Giả sử hình chữ nhật có các đỉnh lần lượt là 
// 𝐴(𝑥1,𝑦1),𝐵(𝑥2,𝑦1),𝐶(𝑥2,𝑦2),𝐷(𝑥1,𝑦2) và điểm cần kiểm tra có tọa độ là I(𝑥i,𝑦i).

#include <iostream>
#include <cmath>
using namespace std;
class Diem
{
private:
   int x, y ;
public: 
   void setXY (int X,int Y){
      x = X;
      y = Y;
   }
   int getX (){
      return x;
   }
   int getY (){
      return y;
   }
   double khoangcach ( Diem d2){
      return sqrt((x - d2.getX())*(x- d2.getX())+(y-d2.getY())*(y-d2.getY()));
   }
};

class HCN
{
private:
    Diem A, B ,C ,D, I;
public:

   void setDiem(Diem a, Diem b, Diem c, Diem d) {
        A = a;
        B = b;
        C = c;
        D = d;
   }

   void setI (Diem i){
      I = i;
   }

   double DienTich (){
        double AB = A.khoangcach(B);
        double BC = B.khoangcach(C);
        return AB*BC ;
   }

   double ChuVi (){
         double AB = A.khoangcach(B);
         double BC = B.khoangcach(C);
         return (AB+BC)*2;
   }

   void KtVitri (){
      if (A.getX() <= I.getX() && I.getX()<=B.getX() && B.getY() <= I.getY() && I.getX()<=C.getY() ){
         cout << "\nDiem nam trong hoac tren hcn.";
      } else
         cout << "\nDiem nam ngoai hcn.";
   }
};

int main (){
   Diem A, B, C, D, I;
   HCN hcn;
   A.setXY(0, 0);
   B.setXY(4, 0);
   C.setXY(4, 3);
   D.setXY(0, 3);
   hcn.setDiem(A, B, C, D);
   
   cout << "Dien tich: "<< hcn.DienTich();
   cout << "\nChu vi: "<< hcn.ChuVi();
    
   I.setXY(2,2);
   hcn.KtVitri();

}