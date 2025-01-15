import numpy as np
from scipy.linalg import sqrtm

# 행렬 A 정의
A = np.array([[1, -2], [2, 2]])

# A의 제곱근 계산
# np.sqrt()는 성분별로 제곱근을 구해서, 행렬 전체의 제곱근과 다르다.
A_sqrt = sqrtm(A)

print("A의 제곱근:")
print(A_sqrt)

# A의 역제곱근은 바로 함수 사용 불가
# 역행렬 구한 후 제곱근을 출력
A_inv = np.linalg.inv(A)
A_inv_sqrt = sqrtm(A_inv)
print("A의 역제곱근:")
print(A_inv_sqrt)


