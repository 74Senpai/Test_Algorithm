using System;

namespace GiaiToanCoBan
{
    class Program
    {
        static void tachDauNgoac_V1(string phepToan, string phepToanGoc)
        {
            // int viTriMoNgoac = phepToan.LastIndexO("(");
            // int viTriDongNgoac = phepToan.IndexOf(")");
            // string phepToanTrongNgoac = phepToan.Substring( viTriMoNgoac, (viTriDongNgoac+1) -  viTriMoNgoac);
            int viTriMoNgoac = phepToan.IndexOf("(");
            int viTriDongNgoac = phepToan.IndexOf(")");
            
            string phepToanTrongNgoac = phepToan.Substring(viTriMoNgoac , viTriDongNgoac + 1 - (viTriMoNgoac));
            if(phepToanTrongNgoac.IndexOf("(") != -1 && phepToanTrongNgoac.IndexOf("(") != 0)
            {
                string phepToanPhiaSau = phepToan.Substring(viTriDongNgoac + 1);
                int viTriDongNgoacCha = phepToanPhiaSau.IndexOf(")");
                string phepToanTrongNgoacCha;
                if(viTriDongNgoacCha == 0)
                {
                    phepToanTrongNgoacCha = phepToanPhiaSau.Substring(0, 1);
                }else{
                    phepToanTrongNgoacCha = phepToanPhiaSau.Substring(0, viTriDongNgoacCha);
                }
                viTriDongNgoac = viTriDongNgoac + viTriDongNgoacCha + 1;
                phepToanTrongNgoac = phepToanTrongNgoac + phepToanTrongNgoacCha;   
                tachDauNgoac_V1(phepToanTrongNgoac, phepToanGoc);
            }
            Console.WriteLine("Phep toan: " + phepToan);
            Console.WriteLine("Vi tri mo ngoac: " + viTriMoNgoac);
            Console.WriteLine("Vi tri dong ngoac: " + viTriDongNgoac);
            Console.WriteLine("Phep toan trong ngoac: " + phepToanTrongNgoac);

        }
        static double tinhToan(string phepToan)
        {
            phepToan = phepToan.Trim();
            
            if (phepToan[0] == '-')
            {
                return -tinhToan(phepToan.Substring(1));
            }

            int index = phepToan.LastIndexOf("+");
            if (index > 0) return tinhToan(phepToan.Substring(0, index)) + tinhToan(phepToan.Substring(index + 1));

            index = phepToan.LastIndexOf("-");
            if (index > 0) return tinhToan(phepToan.Substring(0, index)) - tinhToan(phepToan.Substring(index + 1));

            index = phepToan.LastIndexOf("%");
            if (index > 0) return tinhToan(phepToan.Substring(0, index)) % tinhToan(phepToan.Substring(index + 1));

            index = phepToan.LastIndexOf("*");
            if (index > 0) return tinhToan(phepToan.Substring(0, index)) * tinhToan(phepToan.Substring(index + 1));

            index = phepToan.LastIndexOf("/");
            if (index > 0) return tinhToan(phepToan.Substring(0, index)) / tinhToan(phepToan.Substring(index + 1));

            return double.Parse(phepToan);
        }
        static string chuanHoaPhepToan(string phepToan)
        {
            phepToan = phepToan.Trim();
            phepToan = phepToan.Replace(" ", "");
            phepToan = phepToan.Replace("(-", "(0-");
            phepToan = phepToan.Replace("--", "+");
            phepToan = phepToan.Replace("+-", "-");
            phepToan = phepToan.Replace("*-", "*0-");
            phepToan = phepToan.Replace("/-", "/0-");
            phepToan = phepToan.Replace("%-", "%0-");
            return phepToan;
        }
        
        static void tachDauNgoac_V2(string phepToan)
        {
            if(phepToan.IndexOf("(") == -1)
            {
                phepToan = chuanHoaPhepToan(phepToan);
                Console.WriteLine("Phep toan: " + phepToan);
                Console.WriteLine("Ket qua: " + tinhToan(phepToan));
                return;
            }
            int[][] cacDauNgoac = new int[(phepToan.Length - 1) / 3][]; 
            for (int i = 0; i < cacDauNgoac.Length; i++)
            {
                cacDauNgoac[i] = new int[2];
            }

            int index = 0;
            for (int i = 0; i < phepToan.Length; i++)
            {
                if(phepToan[i] == '(')
                {
                    cacDauNgoac[index][0] = i;
                    index++;
                }else if(phepToan[i] == ')')
                {
                    cacDauNgoac[index][1] = i;
                    index++;
                }
            }
            
            for (int i = 0; i < cacDauNgoac.Length; i++)
            {
                Console.WriteLine("Vị trí mở ngoặc: " + cacDauNgoac[i][0]);
                Console.WriteLine("Vị trí đóng ngoặc: " + cacDauNgoac[i][1]);
            }

            int viTriMoNgoac_Tmp = 0;
            int viTriDongNgoac_Tmp = 0;
            for(int i = 0; i < cacDauNgoac.Length; i++)
            {
                if(cacDauNgoac[i][0] != 0)
                {
                    viTriMoNgoac_Tmp = cacDauNgoac[i][0];
                }
                if(cacDauNgoac[i][1] != 0)
                {
                    viTriDongNgoac_Tmp = cacDauNgoac[i][1];
                    Console.WriteLine("Phep toan trong ngoac: " + phepToan.Substring(viTriMoNgoac_Tmp, viTriDongNgoac_Tmp - viTriMoNgoac_Tmp + 1));
                    Console.WriteLine("Ket qua phep toan trong ngoac: " + tinhToan(phepToan.Substring(viTriMoNgoac_Tmp + 1, viTriDongNgoac_Tmp - viTriMoNgoac_Tmp - 1)));
                    tachDauNgoac_V2(phepToan.Substring(0, viTriMoNgoac_Tmp) + tinhToan(phepToan.Substring(viTriMoNgoac_Tmp + 1, viTriDongNgoac_Tmp - viTriMoNgoac_Tmp - 1)) + phepToan.Substring(viTriDongNgoac_Tmp + 1));
                    break;
                }
            }
        }


        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string phepToan = "56+4-(2+3+(-15)+1)*2-(4+3)+(7*0)";// 2+3+(-15)+1
            Console.WriteLine("Phep toan: " + phepToan);
            // tachDauNgoac_V1(phepToan, phepToan);
            tachDauNgoac_V2(phepToan);
            string test = "2+3+1*5-2*3+1";
            // double kq = tinhToan(test);
            // Console.WriteLine("Ket qua: " + kq);
            // Stop exit program
            Console.ReadLine();
        }
    }
}