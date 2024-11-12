import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
penguins = sns.load_dataset('penguins')

# 경쾌한 색상 조합 설정
palette = ['#FF69B4', '#00CED1', '#FFA500']  # 핫핑크, 터콰이즈, 주황

# 1. 종별 개체수 막대 그래프
plt.figure(figsize=(10, 6))
sns.countplot(data=penguins, x='species', palette=palette)
plt.title('Number of Penguins by Species')
plt.show()

# 2. 바이올린 플롯
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.violinplot(data=penguins, x='species', y='bill_length_mm', ax=axes[0,0], palette=palette)
sns.violinplot(data=penguins, x='species', y='bill_depth_mm', ax=axes[0,1], palette=palette)
sns.violinplot(data=penguins, x='species', y='flipper_length_mm', ax=axes[1,0], palette=palette)
sns.violinplot(data=penguins, x='species', y='body_mass_g', ax=axes[1,1], palette=palette)

plt.tight_layout()
plt.show()

# 3. 산점도
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', 
                hue='species', palette=palette)
plt.title('Bill Length vs Bill Depth by Species')
plt.show()