# Select a principal eigenvector via NumPy
# to be used as a template (copy & paste) script

import numpy as np

# set A to be your matrix
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


eig_vals, eig_vecs = np.linalg.eig(A)
idx = np.absolute(eig_vals).argsort()[::-1]  # decreasing order
sorted_eig_vals = eig_vals[idx]
sorted_eig_vecs = eig_vecs[:, idx]

principal_eig_vec = sorted_eig_vecs[:, 0]  # eigvec with largest eigval

normalized_pr_eig_vec = np.real(principal_eig_vec / np.sum(principal_eig_vec))
print(normalized_pr_eig_vec)  # eigvec that sums up to one
