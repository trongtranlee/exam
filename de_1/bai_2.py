# Viết hàm "checkPrime" trả về kiểu dữ liệu bool để kiểm tra 1 số có phải số nguyên tố không
# (số nguyên tố là số chỉ chia hết cho 1 và chính nó). Nếu có trả về True, nếu không trả về False.

# Nhập một số nguyên từ bàn phím vào lưu vào biến N
n = int(input("Nhập một số nguyên N: "))
def checkPrime(number):
  if number <= 1:
    return False
  for i in range(2, int(number**0.5) + 1): #Chỉ cần kiểm tra đến n/2 + 1 chứ không cần kiểm tra đến n tránh lãng phí tài nguyên
    if number % i == 0:
      return False
  return True

# Sử dụng hàm checkPrime để tính tổng số nguyên tố từ trong khoảng từ [1,N] và in kết quả ra màn hình
tong_so_nguyen_to = 0
for i in range(2, n + 1): # Bắt đầu từ 2 vì 1 không phải số nguyên tố
  if checkPrime(i): #Nếu kết quả trả về True thì cộng vào tong_so_nguyen_to
    tong_so_nguyen_to += i

print(f"Tổng các số nguyên tố từ 1 đến {n} là: {tong_so_nguyen_to}")