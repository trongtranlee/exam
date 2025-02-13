import math  # Import math for comparison later (optional)

# Viết hàm "myFactorial" tính giá trị của n! (không sử dụng thư viện, hàm có sẵn trong Python)
def myFactorial(n):
  if n < 0:
    return "Giai thừa không xác định cho số âm"
  elif n == 0:
    return 1
  else:
    factorial = 1
    for i in range(1, n + 1):
      factorial *= i
    return factorial

# Ví dụ sử dụng hàm myFactorial
# print(f"5! = {myFactorial(5)}")

# Tính e^x theo công thức sau sử dụng hàm "myFactorial"
# e^x = Σ (x^n / n!) từ n=0 đến ∞

# Dừng vòng lặp tính toán khi sai số nhỏ hơn 0.001, in kết quả ra màn hình.

# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị x để tính e^x: "))

e_x_approx = 0.0  # Khởi tạo giá trị gần đúng của e^x
n = 0
term = 1.0       # Số hạng đầu tiên (n=0): x^0 / 0! = 1/1 = 1
epsilon = 0.001  # Sai số mong muốn

while abs(term) >= epsilon:
  e_x_approx += term
  n += 1
  term = (x**n) / myFactorial(n)

# In kết quả ra màn hình
print(f"Giá trị e^{x} tính theo công thức chuỗi là: {e_x_approx}")

# Kiểm tra với hàm math.exp để so sánh (tùy chọn)
gia_tri_math_exp = math.exp(x)
print(f"Giá trị e^{x} tính bằng math.exp là: {gia_tri_math_exp}")
print(f"Sai số giữa hai kết quả: {abs(e_x_approx - gia_tri_math_exp)}")