# DS-440 Final Project

## Project Outline
### 1. Introduction & Problem Definition
- Brief overview of the project
- Clearly defined problem statement or objective
- Importance and relevance of the chosen problem in the context of data mining

### 2. Methodology
2.1 Dataset and Initial Statistics
- **2.1.1 Statistical Summary**
    - Summary statistics of the dataset (mean, median, standard deviation, etc.)
    - Identify key features and their distributions
- **2.1.2 Initial Data Visualization**
    - Visual representation of data through charts, graphs, and plots
    - Preliminary insights gained from initial visualization
    - 2.2 Technical Approaches
- **2.2.1 Supervised Learning Approach (at least two approaches)**
    - Description of the selected supervised learning algorithms
    - Training and testing procedures
    - Parameter tuning and optimization
- **2.2.2 Unsupervised Learning Approach (at least two approaches)**
    - Explanation of chosen unsupervised learning algorithms
    - Clustering or dimensionality reduction techniques employed
    - Any preprocessing steps taken before applying the algorithms


### 3. Evaluation & Discussion

**3.1 Comparison of Supervised Learning Methods**
- Evaluation metrics used (accuracy, precision, recall, F1-score, etc.)
- Comparative analysis of results from different supervised learning approaches
- Discussion on the strengths and weaknesses of each approach

**3.2 Comparison of Unsupervised Learning Methods**
- Evaluation criteria specific to unsupervised learning (silhouette score, inertia, etc.)
- Comparative analysis of results from different unsupervised learning approaches
- Insightful discussion on the appropriateness of each approach for the given problem

### 4. Conclusion
- Summary of key findings and insights from the project
- Reflection on the effectiveness of the chosen methodologies
- Suggestions for future work or improvements in the analysis

### Code/Report Walkthrough
- Detailed walkthrough of the implemented code
- Highlighting key sections, functions, and algorithms used
- Explanation of any challenges faced and solutions implemented
- Visual aids or code snippets to enhance understanding


### **Final Project Report Sample Outline**

As per [this Canvas announcement](https://erau.instructure.com/courses/163647/discussion_topics/2877409):

1. Introduction & Problem Definition
2. Methodology
    - (2.1) Dataset and Initial Statistics
        - (2.1.1)Statistical Summary
        - (2.1.2)Initial Data Visualization
    - 2.2 Technical Approaches.
        - (2.2.1) Supervised Learning Approach (at least two approaches)
        - (2.2.2) Unsupervised Learning Approach (at least two approaches)
3. 3 Evaluation & Discussion
    - (3.1) Comparison of Supervised Learning Methods
    - (3.2) Comparison of Unsupervised Learning Methods
4. 4 Conclusion
## Checklist
### Progress Reports
- [x] Final Project Initialization
- [x] Final Project Progress Report #1
- [x] Final Project Progress Report #2
- [x] Final Project Progress Report #3

### Main Tasks
- [x]  Compile the final project outline
- [x]  Create a checklist for the final project
- [x]  Finalize [preliminary notes and ideas](https://www.notion.so/Our-Data-Ideas-Notes-etc-1e53e3f0321f44f4a05973f688a95b8a?pvs=21) for the project (see [emails](https://www.notion.so/Questions-Concerns-Conversations-835258720cd94723b28005ac2daceca4?pvs=21))
- [x]  Research and decide on [machine learning models to apply](https://www.notion.so/Final-Project-DS440-92fd14092a094b65b0df6f1a7907a046?pvs=21)
- [x]  Review and understand the columns in the dataset
- [ ]  Visualize the dataset using `seaborn` or `matplotlib`
    - [ ]  Correlation plot
    - [ ]  Pie chart(s)
- [ ]  Visualize machine learning models with `sklearn` or other libraries
- [ ]  Research and gather relevant sources for the project
- [ ]  Write [final report](https://www.overleaf.com/project/654fd934d42bfeadc125a7e7) (in $\LaTeX$)

## Data

This [dataset](https://data.ct.gov/Education/School-Attendance-by-Student-Group-and-District-20/t4hx-jd4c) includes the attendance rate for public school students PK-12 by student group and by district during the 2021-2022 school year.

**Student groups include**:

- Students experiencing homelessness
- Students with disabilities
- Students who qualify for free/reduced lunch
- English learners
- All high-needs students
- Non-high-needs students
- Students by race/ethnicity (Hispanic/Latino of any race, Black or African American, White, All other races)

Attendance rates are provided for each student group by district and for the state. Students considered high needs include English language learners, who receive special education, or who qualify for free and reduced lunch.

When no attendance data is displayed in a cell, data have been suppressed to safeguard student confidentiality, or to ensure that statistics based on a minimal sample size are not interpreted as equally representative as those based on a sufficiently larger sample size, for [more information on CSDE data suppression policies](http://edsight.ct.gov/relatedreports/BDCRE%20Data%20Suppression%20Rules.pdf).


## Sources
### Sci-Kit Learn

- [1. Supervised learning — scikit-learn 1.3.2 documentation](https://scikit-learn.org/stable/supervised_learning.html)
- [1.4. Support Vector Machines — scikit-learn 1.3.2 documentation](https://scikit-learn.org/stable/modules/svm.html#regression)
- [1.10. Decision Trees — scikit-learn 1.3.2 documentation](https://scikit-learn.org/stable/modules/tree.html)
- [sklearn.ensemble.RandomForestRegressor — scikit-learn 1.3.2 documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
- [1.10. Decision Trees — scikit-learn 1.3.2 documentation](https://scikit-learn.org/stable/modules/tree.html#regression)
    - [Decision Tree Regression — scikit-learn 1.3.2 documentation](https://scikit-learn.org/stable/auto_examples/tree/plot_tree_regression.html#sphx-glr-auto-examples-tree-plot-tree-regression-py)

### Pandas

- [pandas.DataFrame.replace — pandas 2.1.3 documentation (pydata.org)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html)

### Matplotlib

- [Top 50 matplotlib Visualizations - The Master Plots (w/ Full Python Code) | ML+ (machinelearningplus.com)](https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/)
