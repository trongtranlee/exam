#Viet hàm "tong2So" nhận vào 2 số thực và trả về tổng 2 số
#Gọi hàm "tong2So" với 2 số bất kỳ và in ra màn hình
def tong2So(so_thu_nhat, so_thu_hai): #Chỗ này truyền vào 2 giá trị là số thứ 1 và số thứ 2
  return so_thu_nhat + so_thu_hai  #Trả về kết quả là tổng 2 số


so1 = 10.5 #Chọn random số thứ 1
so2 = 5.2 #Chọn random ố thứ 2
tong = tong2So(so1, so2) # Gọi hàm "tong2So" với 2 số bất kỳ và in ra màn hình

print(f"Tổng của {so1} và {so2} là: {tong}")