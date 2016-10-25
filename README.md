## Map Reduce Example for Sparse Matrix Multiplication

Map Reduce paradigm is usually used to aggregate data at a large scale. To put it in a crude analogy, Map Reduce is analogous to the `GROUP BY` statement in SQL. The input files are processed in the mapper such that a key-value pair is emitted, with the key being the aggregation key on which we want to aggregate our data. This key is hashed such that all occurences of a key go to a single reducer as input. All the instances of a keys to a reducer are sorted so that all the keys are grouped together, when they are being processed by the reducer.

While writing Map Reduce jobs for hadoop using python, they can be written such that the mapper script and the reducer script takes input from `STDIN`. Also the output of both mapper and reducer is to `STDOUT`. 

### Matrix Multiplication

We use a sparse representation of matrix to denote it. This representation looks like this for two matrices `A` & `B`

```bash
A,0,0,63
A,0,1,45
A,0,2,93
A,0,3,32
A,0,4,49
A,1,0,33
A,1,3,26
A,1,4,95
A,2,0,25
A,2,1,11
A,2,3,60
A,2,4,89
A,3,0,24
A,3,1,79
A,3,2,24
A,3,3,47
A,3,4,18
A,4,0,7
A,4,1,98
A,4,2,96
A,4,3,27
B,0,0,63
B,0,1,18
B,0,2,89
B,0,3,28
B,0,4,39
B,1,0,59
B,1,1,76
B,1,2,34
B,1,3,12
B,1,4,6
B,2,0,30
B,2,1,52
B,2,2,49
B,2,3,3
B,2,4,95
B,3,0,77
B,3,1,75
B,3,2,85
B,4,1,46
B,4,2,33
B,4,3,69
B,4,4,88
```
Here, the first column denotes the matrix whose elements are listed. The second and third column contain row and column indices for non zero values in that matrix, finally the fourth column denotes the value at the particular index.

