# Nhập một số nguyên từ bàn phím vào lưu vào biến N
n = int(input("Nhập một số nguyên N: "))

# Viết hàm "chiaHetCho2" nhận vào một số nguyên dương, trả về True nếu số đó chia hết cho 2
# và False nếu không chia hết cho 2.
def chiaHetCho2(number):
  if number % 2 == 0:
    return True
  else:
    return False

# Sử dụng hàm chiaHetCho2 để tính tổng các số chẵn trong khoảng từ [1,N] và tính tổng các số
# lẻ trong khoảng từ [1,N] (2 tổng riêng biệt cho số chẵn và số lẻ), in kết quả ra màn hình.
tong_chan = 0
tong_le = 0

for i in range(1, n + 1):
  if chiaHetCho2(i): # Kiểm tra nếu số i là số chẵn
    tong_chan += i
  else: # Nếu không phải số chẵn thì là số lẻ
    tong_le += i

print(f"Tổng các số chẵn từ 1 đến {n} là: {tong_chan}")
print(f"Tổng các số lẻ từ 1 đến {n} là: {tong_le}")