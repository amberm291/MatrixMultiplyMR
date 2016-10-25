## Map Reduce Example for Sparse Matrix Multiplication

Map Reduce paradigm is usually used to aggregate data at a large scale. To put it in a crude analogy, Map Reduce is analogous to the `GROUP BY` statement in SQL. The input files are processed in the mapper such that a key-value pair is emitted, with the key being the aggregation key on which we want to aggregate our data. This key is hashed such that all occurences of a key go to a single reducer as input. All the instances of a keys to a reducer are sorted so that all the keys are grouped together, when they are being processed by the reducer.

While writing Map Reduce jobs for hadoop using python, they can be written such that the mapper script and the reducer script takes input from `STDIN`. Also the output of both mapper and reducer is to `STDOUT`. 

### Matrix Multiplication

We use a sparse representation of matrix to denote it. This representation looks like this for two matrices `A` & `B`

```bash
A,0,0,63
A,0,1,45
A,0,2,93
.
.
B,0,0,63
B,0,1,18
.
.
B,4,4,88
```
Here, the first column denotes the matrix whose elements are listed. The second and third column contain row and column indices for non zero values in that matrix, finally the fourth column denotes the value at the particular index.

The entire input is given in the file `input.txt`. The size of both matrices in the file is `5x5` 

Note: In the input, each input line should always be tagged with the matrix it belongs. For e.g. in the input above, each line contains whether the entry belongs to `A` or `B`.

### Mapper

For a matrix multiplication of the form `AB`, we must provide in the mapper, the number of rows of A, referenced as `row_a` in the code, and the number of columns of B, referenced as `col_b` (The number of columns of A and number of rows of B are always same, else multiplication won't be possible). In this example, I have fixed the values of `row_a` and `col_b` as 5 in the cache file `cache.txt`. 

Consider the following snippet from the mapper:

```bash
if matrix_index == "A":
	for i in xrange(0,col_b):
		key = row + "," + str(i)
		print "%s\t%s\t%s"%(key,col,value)
else:
	for j in xrange(0,row_a):
		key = str(j) + "," + col 
		print "%s\t%s\t%s"%(key,row,value)
```

Basically, if the input line is from `A`, then we take the row index, iterate from 0 to `col_b` and set the key as `(row index,i)`. We set the value for the key as a tuple of column index and value at the index. In case the input is `B`, we iterate from 0 to `row_a` and set the key as `(j,column index)` and the value as a tuple of row index and value.

### Reducer

In the reducer, for each key we form a list of tuples of values emitted from the mapper. We sort this list with the first element, which is the index, as each tuple as the sorting key. Once, the list is sorted, we scan the list to find all consecutive tuples having the same index. Such tuples values are multiplied and added in the result. The following piece of code from the reducer does that - 

```bash
value_list = sorted(value_list,key=itemgetter(0))
i = 0
result = 0
while i < len(value_list) - 1:
    if value_list[i][0] == value_list[i + 1][0]:
        result += value_list[i][1]*value_list[i + 1][1]
        i += 2
    else:
        i += 1
```

### Testing the mapper and reducer

To test the mapper and reducer, for input values in `input.txt`, we use the following bash command

```bash
$ cat input.txt | python mapper.py | sort | python reducer.py
```

This will print the output of reducer in the terminal console. For the file `input.txt`, after running the above command, we get the output as

```bash
0,0,11878
0,1,14044
0,2,16031
0,3,5964
0,4,15874
1,0,4081
1,1,6914
1,2,8282
1,3,7479
1,4,9647
2,0,6844
2,1,9880
2,2,10636
2,3,6973
2,4,8873
3,0,10512
3,1,12037
3,2,10587
3,3,2934
3,4,5274
4,0,11182
4,1,14591
4,2,10954
4,3,1660
4,4,9981
```



