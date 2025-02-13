import math

# Nhập giá trị x, đảm bảo |x| < 1
while True:
    x = float(input("Nhập giá trị x (|x| < 1): "))
    if abs(x) < 1:
        break
    else:
        print("Giá trị x không hợp lệ. Vui lòng nhập lại giá trị x sao cho |x| < 1.")

# Khởi tạo tổng và số hạng đầu tiên
tong = 0.0
term = -x  # Số hạng đầu tiên là -x (n=1)
n = 1

# Sai số mong muốn
epsilon = 0.001

# Vòng lặp tính toán cho đến khi sai số nhỏ hơn epsilon
while abs(term) >= epsilon:
    tong += term
    n += 1
    term = - (x**n) / n # Số hạng tiếp theo

# In kết quả ra màn hình
print(f"Giá trị ln(1 - {x}) tính theo công thức chuỗi là: {tong}")

# Kiểm tra với hàm math.log để so sánh (tùy chọn)
gia_tri_math_log = math.log(1 - x)
print(f"Giá trị ln(1 - {x}) tính bằng math.log là: {gia_tri_math_log}")
print(f"Sai số giữa hai kết quả: {abs(tong - gia_tri_math_log)}")