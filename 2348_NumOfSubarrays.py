# Công thức tổng quát cho n với n là số số 0 liên tiếp:
# total_sub = n + n - 1 + n - 2 + ... + 1
# hay 
# total_sub = 1 + 2 + ... + n
# hướng giải
# B1: duyệt mảng
# B1.1 : tìm thấy 0 -> đếm n -> khác 0 -> dừng đếm
# B1.2 : hết mảng -> dừng đếm
# B1.2.1 : n bằng 0 -> dừng chương trình
# B2: tính total_sub theo công thức, cộng vào kết quả, cập nhật lại n(độ dài)
# B3: quay lại B1

# Theo các bước, công thức ->
class Ver1:
    # PASS: 65ms, 28.2MB
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        total_sub = 0
        count = 0
        for x in nums:
            if x == 0:
                count += 1
            else:
                for i in range(count + 1):
                    total_sub += i
                count = 0
        if count > 0:
            for i in range(count + 1):
                    total_sub += i

        return total_sub

# Cách tối ưu hơn: 
# Thay vì đếm n rồi mới tính thì chỉ cần thêm n vào kết quả nếu như tìm thấy 0
# VD: nếu có 1 đoạn 0,0,0 thì n sẽ được thêm vào total_sub như sau : 1 + 2 + 3
class Ver2:
    # PASS: 21ms, 28.38MB
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        res = 0
        count = 0
        for x in nums:
            if x == 0:
                count += 1
                res += count
            else:
                count = 0
        return res