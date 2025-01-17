# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YHDI7jqdeyYbyUcRlyN_E66Dq0hwlQM_
"""



import numpy as np
import matplotlib.pyplot as plt

# X qiymatlari uchun oraliq
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Sinus funksiyasi
y = np.sin(x)

# Grafikni chizish
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r"$y = \sin(x)$", color="blue")

# Koordinata o'qlari
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # gorizontal chiziq
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # vertikal chiziq

# Grafikning sarlavhasi va o'qlar nomlari
plt.title("Sinus funksiyasining grafigi", fontsize=14)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$y$", fontsize=12)

# O'qlar bo'yicha shkalalar va ularning belgilari
plt.xticks(
    ticks=[-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
    labels=[r"$-2\pi$", r"$-\pi$", "$0$", r"$\pi$", r"$2\pi$"]
)
plt.yticks(ticks=[-1, 0, 1])

# Panjara va afsona
plt.grid(alpha=0.5)
plt.legend(fontsize=12)

# Grafikni ko'rsatish
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Tasodifiy nuqtalar soni
num_points = 100

# X va Y koordinatalari uchun tasodifiy qiymatlar generatsiyasi
x = np.random.rand(num_points) * 10  # [0, 10] oraliqda
y = np.random.rand(num_points) * 10  # [0, 10] oraliqda

# Scatter grafi
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color="blue", alpha=0.7, edgecolor="black", label="Tasodifiy nuqtalar")

# Grafikning sarlavhasi va o'qlar nomlari
plt.title("Tasodifiy nuqtalar scatter grafigi", fontsize=14)
plt.xlabel("$X$", fontsize=12)
plt.ylabel("$Y$", fontsize=12)

# Panjara va afsona
plt.grid(alpha=0.3)
plt.legend(fontsize=12)

# Grafikni ko'rsatish
plt.show()