import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import DBSCAN, AgglomerativeClustering, KMeans
from sklearn.manifold import TSNE
from sklearn.metrics import pairwise_distances

# col names
col_names = [
    "pregnant",
    "glucose",
    "bp",
    "skin",
    "insulin",
    "bmi",
    "pedigree",
    "age",
    "label",
]

feature_cols = [
    "pregnant",
    "skin",
    "insulin",
    "bmi",
    "age",
    "glucose",
    "bp",
    "pedigree",
]

pima = pd.read_csv("diabetes.csv", header=0, names=col_names)
X = pima[feature_cols]  # Features
y = pima.label  # Target variable
pima.head()


Embedded = TSNE(
    n_components=2, learning_rate="auto", init="random", perplexity=5
).fit_transform(X)

colorMp = list(y.values)

print(Embedded.shape)

plt.scatter(Embedded[:, 0], Embedded[:, 1], c=colorMp, s=8)

"""## Let's see how *K-Means* group the data"""


kmeans = KMeans(n_clusters=4, random_state=0, n_init="auto").fit(X)
plt.figure()
plt.scatter(Embedded[:, 0], Embedded[:, 1], c=kmeans.labels_, s=8)

sseLst = []
for k in range(20):
    kmeans = KMeans(n_clusters=k + 1, random_state=0, n_init="auto").fit(X)
    sse = kmeans.inertia_
    sseLst.append(sse)
    print(f"SSE of Given data when k = {k} is {sse}")
plt.figure()
plt.stem(np.arange(1, 21, 1), sseLst, basefmt="k:")

kmeans = KMeans(n_clusters=4, random_state=0, n_init="auto").fit(X)
clf = kmeans

pairwisedist = pairwise_distances(X, metric="cosine")
sorted_pairwisedist = pairwisedist[np.argsort(clf.labels_)][:, np.argsort(clf.labels_)]
labels = clf.labels_[np.argsort(clf.labels_)]

sorted_pairwisedist = sorted_pairwisedist / np.max(sorted_pairwisedist)
sorted_similarity = 1 - sorted_pairwisedist / np.max(sorted_pairwisedist)

# plotting
import matplotlib.pyplot as plt

plt.figure()
plt.imshow(sorted_similarity, cmap="jet", interpolation="none")
plt.colorbar()

corrhist = []
ssehist = []
data = X.copy()

# specify different ranges for each column
ranges = [(data[col].min(), data[col].max()) for col in data.columns]
for seed in range(0, 100):
    np.random.seed(seed)
    randomdata = np.random.default_rng().uniform(
        low=ranges[0][0], high=ranges[0][1], size=(100, 1)
    )

    for r in ranges[1:]:
        randomdata = np.concatenate(
            (randomdata, np.random.randint(low=r[0], high=r[1], size=(100, 1))), axis=1
        )

    randomdf = pd.DataFrame(randomdata)

    scaledranddf = randomdf
    clfr = KMeans(n_clusters=4, random_state=0, n_init="auto").fit(scaledranddf)
    labels = clfr.labels_[np.argsort(clfr.labels_)]

    pairwisedistr = pairwise_distances(scaledranddf, metric="cosine")
    sorted_pairwisedistr = pairwisedist[np.argsort(labels)][:, np.argsort(labels)]

    incidence_matrixr = np.zeros_like(sorted_pairwisedistr)
    for i in range(len(labels)):
        for j in range(len(labels)):
            incidence_matrixr[i, j] = int(labels[i] == labels[j])

    corrhist.append(
        np.corrcoef(sorted_pairwisedistr.flatten(), incidence_matrixr.flatten())[0, 1]
    )
    ssehist.append(clfr.inertia_)

plt.hist(ssehist, bins=30)

clf = KMeans(n_clusters=4, random_state=0, n_init="auto").fit(X)

plt.axvline(np.mean(ssehist), color="red", linestyle="dashed", linewidth=1)
plt.axvline(clf.inertia_, color="green", linestyle="dashed", linewidth=1)
plt.title("SSE of Original data vs 100 Random datasets")
plt.xlabel("SSE")
plt.show()


clustering = DBSCAN(eps=30, min_samples=5).fit(X)
plt.scatter(Embedded[:, 0], Embedded[:, 1], c=clustering.labels_, s=8)
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
model = model.fit(X)


def plot_dendrogram(model, **kwargs):
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    dendrogram(linkage_matrix, **kwargs)


plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()

model = AgglomerativeClustering(distance_threshold=None, n_clusters=4)

model = model.fit(X)
plt.scatter(Embedded[:, 0], Embedded[:, 1], c=model.labels_, s=8)


model = AgglomerativeClustering(distance_threshold=None, n_clusters=4)
model = model.fit(X)
clf = model

pairwisedist = pairwise_distances(X, metric="cosine")
sorted_pairwisedist = pairwisedist[np.argsort(clf.labels_)][:, np.argsort(clf.labels_)]
labels = clf.labels_[np.argsort(clf.labels_)]
sorted_pairwisedist = sorted_pairwisedist / np.max(sorted_pairwisedist)
sorted_similarity = 1 - sorted_pairwisedist / np.max(sorted_pairwisedist)

plt.figure()
plt.imshow(sorted_similarity, cmap="jet", interpolation="none")
plt.colorbar()

X2 = X.copy()
X2["cluster"] = (model.labels_ + 1) * 100
X2["True_Label"] = (y + 1) * 100
X2

X2 = X2.sort_values(["cluster", "True_Label"])
X_new = X2.iloc[:, :]
X_new

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.imshow(X_new.values, aspect="auto", interpolation="none")
plt.colorbar()
plt.show()

X_new.columns

ClusterAverage = X_new.groupby(["cluster"])[
    "pregnant", "skin", "insulin", "bmi", "age", "glucose", "bp", "pedigree"
].mean()
ClusterAverage

plt.imshow(ClusterAverage.values, aspect="auto", interpolation="none")
plt.colorbar()
plt.show()

"""#### Let's try another popular diagram, the Radar Plot."""

from scipy import stats

values = np.array([])
variables = []
clusters = []
df = ClusterAverage.copy()

for r in range(df.shape[0]):
    rowContent = df.iloc[r, :]
    values = np.append(values, rowContent, axis=0)
    variables.extend(df.columns.values.tolist())
    clusters.extend([str(r + 1)] * df.shape[1])

df = pd.DataFrame(dict(value=values, variable=variables, group=clusters))

fig = px.line_polar(df, r="value", theta="variable", line_close=True, color="group")
fig.update_traces(fill="toself")

fig.show()


values = np.array([])
variables = []
clusters = []
df = ClusterAverage.copy()
for c in df.columns:
    df[c] = stats.zscore(df[c])

for r in range(df.shape[0]):
    rowContent = df.iloc[r, :]
    values = np.append(values, rowContent, axis=0)
    variables.extend(df.columns.values.tolist())
    clusters.extend([str(r + 1)] * df.shape[1])

df = pd.DataFrame(dict(value=values, variable=variables, group=clusters))

fig = px.line_polar(df, r="value", theta="variable", line_close=True, color="group")
fig.update_traces(fill="toself", textposition="top center")
fig.show()

ClusterAverage = X_new.groupby(["cluster", "True_Label"])[
    "pregnant", "skin", "insulin", "bmi", "age", "glucose", "bp", "pedigree"
].mean()
ClusterAverage

plt.imshow(ClusterAverage.values, aspect="auto", interpolation="none")
plt.colorbar()
plt.show()

ClusterAverage = X_new.groupby(["True_Label", "cluster"])[
    "pregnant", "skin", "insulin", "bmi", "age", "glucose", "bp", "pedigree"
].mean()

plt.imshow(ClusterAverage.values, aspect="auto", interpolation="none")
plt.colorbar()
plt.show()

X_vis = (
    X_new.groupby(["True_Label", "cluster"])
    .sample(n=3)
    .sort_values(["True_Label", "cluster"])
)

X_vis_true_label = X_vis.loc[:, "True_Label"]
X_vis_cluster = X_vis.loc[:, "cluster"]
X_vis = X_vis.drop(columns=["cluster", "True_Label"])

X_vis.shape


lut = dict(zip(X_vis_true_label.unique(), "rbg"))
row_colors = X_vis_true_label.map(lut)

g = sns.clustermap(
    X_vis,
    figsize=(7, 5),
    dendrogram_ratio=(0.1, 0.2),
    # cbar_pos=(0, .2, .03, .4),
    # cmap="vlag", vmin=0, vmax=400,
    # cbar_pos=(.02, .32, .03, .2),
    row_colors=row_colors,
)

lut = dict(zip(X_vis_true_label.unique(), "rbg"))
row_colors = X_vis_true_label.map(lut)

sns.clustermap(
    X_vis,
    figsize=(7, 5),
    dendrogram_ratio=(0.1, 0.2),
    cbar_pos=(0, 0.2, 0.03, 0.4),
    standard_scale=1,
    # cmap="mako",
    row_colors=row_colors,
)

lut = dict(zip(X_new.True_Label.unique(), "rbg"))
row_colors = X_new.True_Label.map(lut)

sns.clustermap(
    X_new.drop(columns=["cluster", "True_Label"]),
    figsize=(7, 5),
    dendrogram_ratio=(0.1, 0.2),
    cbar_pos=(0, 0.2, 0.03, 0.4),
    cmap="mako",
    standard_scale=1,
    row_colors=row_colors,
)
