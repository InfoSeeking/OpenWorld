# OpenWorld Metrics and Methodology

## 1. Overview

OpenWorld evaluates world models by analyzing the structure of their latent representations, not just their output predictions. The SDK provides a suite of metrics that probe whether a model's internal representations encode meaningful physical structure—such as class separation, invariance to irrelevant features, and geometric organization—rather than relying solely on accuracy or task performance. These metrics are designed to help researchers and developers assess whether a model "understands" physical scenes in a way that generalizes beyond the training set.

## 2. Intervention Design: Background Removal

The background removal intervention tests whether a model's representations depend on background information or focus on foreground dynamics. For each frame in a video, background pixels are identified via background subtraction and replaced with a neutral gray value, preserving only the foreground motion. The shortcut-reliance score measures how much the model's latent representations change when the background is removed. A large change suggests the model relies on background cues; a small change suggests invariance to background.

## 3. The Five Latent Structure Metrics

### Silhouette Score

**Formal definition:**

Let $z_i$ be the embedding for video $i$, and $y_i$ the ground-truth label. For each sample $i$:

$$
s(i) = \frac{b(i) - a(i)}{\max\{a(i), b(i)\}}
$$

where $a(i)$ is the mean intra-class (same label) distance for $i$, and $b(i)$ is the mean nearest-cluster (different label) distance. The overall silhouette score is the mean of $s(i)$ over all samples.

**Plain-English explanation:** Measures how well the embeddings separate the ground-truth classes. High values mean samples are closer to their own class than to other classes.

**Interpretation:**
- High: Embeddings cluster tightly by class, with clear separation.
- Low or negative: Embeddings overlap or are closer to other classes than their own.

**When to use:** Whenever you want to check if your model's representations reflect the ground-truth class structure.

---

### Invariance Score

**Formal definition:**

Let $z_i$ be the embedding for video $i$ and $y_i$ the ground-truth label. The invariance score is:

$$
\mathrm{Inv}(Z, Y) = \text{mean cosine similarity (same label)} - \text{mean cosine similarity (different label)}
$$

**Plain-English explanation:** Measures how similar embeddings are for clips with the same label, compared to those with different labels.

**Interpretation:**
- High: Embeddings are consistent within classes and distinct across classes.
- Low: Embeddings are not class-invariant or are mixed across classes.

**When to use:** To test whether your model encodes class-invariant features.

---

### Nearest Neighbor Geometry Score

**Formal definition:**

Let $z_i$ be the embedding for video $i$. For each $i$, let $\pi(i)$ be the nearest neighbor (excluding $i$). The NN geometry score is:

$$
\mathrm{NNG}(Z) = \text{mean distance to NN with different label} - \text{mean distance to NN with same label}
$$

**Plain-English explanation:** Measures whether the nearest neighbors in embedding space tend to have the same label. High values mean same-label neighbors are closer than different-label neighbors.

**Interpretation:**
- High: Embeddings are organized so that same-label samples are nearest neighbors.
- Low: Nearest neighbors are often from different classes.

**When to use:** To probe local structure and class consistency in the embedding space.

---

### Centroid Gap

**Formal definition:**

Let $C_k$ be the set of embeddings for class $k$, and $\mu_k$ their centroid. The centroid gap is:

$$
\mathrm{CentroidGap}(Z, Y) = \frac{1}{K} \sum_{k=1}^K \|\mu_k - \mu\|^2
$$

where $\mu$ is the global mean embedding, $K$ is the number of classes, and $\|\cdot\|$ is the Euclidean norm.

**Plain-English explanation:** Measures how far apart the class centroids are from the global mean. High values mean class centers are well separated.

**Interpretation:**
- High: Class centroids are far from the global mean, indicating strong class separation.
- Low: Centroids are close together, indicating overlap.

**When to use:** To assess global class separation in the embedding space.

---

### DCI Disentanglement

**Formal definition:**

Let $Z$ be the embedding matrix and $Y$ the ground-truth factors. The DCI metric quantifies Disentanglement, Completeness, and Informativeness as described in the referenced paper.

**Plain-English explanation:** Measures how well the embedding dimensions correspond to independent ground-truth factors (disentanglement), how completely each factor is captured (completeness), and how informative the representation is overall.

**Interpretation:**
- High: Embeddings are disentangled, with each dimension capturing a distinct factor.
- Low: Embeddings are entangled or redundant.

**When to use:** To evaluate the interpretability and factorization of your model's representations.

---

## 4. Limitations

These metrics measure the organizational structure of latent representations, not predictive accuracy or downstream task performance. A model can score well on these metrics without being useful for real-world applications. Use them as diagnostic tools, not as the sole criterion for model selection.
