import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Figure와 Axes 생성 (2행 1열)
fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# 샘플 데이터 생성
data = pd.Series(np.random.rand(5), index=list('abcde'))

# 수직 막대 그래프
data.plot(
    kind='bar', 
    ax=axes[0],
    color='blue',
    alpha=0.7,
    title='Vertical Bar Plot',
    grid=True
)
axes[0].set_ylabel('Values')

# 수평 막대 그래프
data.plot(
    kind='barh',
    ax=axes[1],
    color='red',
    alpha=0.7,
    title='Horizontal Bar Plot',
    grid=True
)
axes[1].set_xlabel('Values')

# 레이아웃 조정
plt.tight_layout()
plt.show()