"""
Reproduce the shortcut exploitation chart from findings/README.md.
Run: python findings/scripts/plot_shortcut_camera_effect.py
"""
import os
import json
import matplotlib.pyplot as plt
import numpy as np

# Load results
with open(os.path.join(os.path.dirname(__file__), '../results.json'), 'r') as f:
    results = json.load(f)

models = ['vjepa2', 'dreamerv3', 'videomae_v2']
model_labels = ['V-JEPA 2', 'DreamerV3', 'VideoMAE v2']
categories = ['overall', 'fixed_camera', 'moving_camera']
cat_labels = ['Overall', 'Fixed Camera', 'Moving Camera']

# Prepare data
values = []
for m in models:
    row = [results['shortcut_exploitation'][m][cat] * 100 for cat in categories]
    values.append(row)
values = np.array(values)  # shape (3, 3)

x = np.arange(len(models))
width = 0.22

fig, ax = plt.subplots(figsize=(6, 4))
for i, (cat, label) in enumerate(zip(categories, cat_labels)):
    ax.bar(x + (i - 1) * width, values[:, i], width, label=label)

ax.set_ylabel('Normalized feature distance change (%)')
ax.set_xticks(x)
ax.set_xticklabels(model_labels)
ax.legend()
ax.set_ylim(0, max(values.flatten()) * 1.2)

# Ensure output directory exists
figures_dir = os.path.join(os.path.dirname(__file__), '../figures')
os.makedirs(figures_dir, exist_ok=True)

plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'shortcut_camera_effect.png'), dpi=150, bbox_inches='tight')
plt.close()
