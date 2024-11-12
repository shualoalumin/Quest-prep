import matplotlib.pyplot as plt
import numpy as np

# 화살표 스타일 리스트
styles = ['-', '->', '-[', '|-|', '-|>', '<-', '<->', 'fancy', 'simple', 'wedge']

# 그래프 설정
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(-1, 4)
ax.set_ylim(-len(styles), 1)

# 각 스타일별 화살표 그리기
for i, style in enumerate(styles):
    ax.annotate('', xy=(3, -i), xytext=(0, -i),
                arrowprops=dict(arrowstyle=style, color='red'))
    ax.text(-0.5, -i, style, ha='right', va='center')

plt.title('Matplotlib Arrow Styles')
ax.grid(False)
ax.set_axis_off()
plt.tight_layout()
plt.show()