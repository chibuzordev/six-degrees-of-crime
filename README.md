- <a href="#bg">Background</a>
- <a href="#pb">Problem</a>
- <a href="#sb">Solution base</a>
- <a href="#md">Method</a>
- <a href="#ad">About the Data</a>
- <a href="#im">Implementation</a>


## <a id="bg">Background</a>
Considering an anti-money laundering (#AML) and crime analysis case: with two suspects; A and C.
* person A is a suspected politician.
* person C is a known terrorist leader. 

Any direct meeting or transaction - financial or otherwise between them would be flagged by the authorities, and heavily probed. 
Nonetheless, to protect their interests, A and C may choose never to transact directly, but instead conduct dealings through safe, respected and unlabeled financial person and authorities; B and D.

### <a id="pb">Problem</a>
Find a way to discover the transitive relationship between politician Mr A and criminal Mr C through their meetings with all possible intermediaries.

### <a id="sb">Solution Base</a>
The Six degrees of seperation would stand as a perfect pointer to pick up on the transaction. 
The method shows how any two element(source and target) can be connected - if possible, within just six steps.

### <a id="md">Method</a>
I frame this as a search problem
- The *states* being the different people iterated over
- The *intial state* is defined by the first person(source)
- The *goal* is the target suspect

Using BFS(breadth-first-search), the shortest path(connection) from one suspect to another can be found 

The *main function* is implemented as a test/driver
- loads the data from directory into memory 
- prompts the user to type in the two names(source & target)

The *person_id_for_name* function 
- retrieves the id for any person

The *shortest_path* function, 
- finds and returns the shortest path link betweent the *source* and the *target* 

The *status* variable - flags pair transactions and link-ups as suspicious " * "

### <a id="ad">About the Data</a>
The data provided is formulated:
- people.csv - the suspects of the case.
- places.csv - points where individuals may have converged.
- appearances.csv - shows the various locations visited by various pairs of people.


### <a id="im">Implementation</a>
```
Loading data...
Data loaded.
Name: Bala Bulu Corn
Name: Shurecan Rigg
The suspects are connected 
There are 3 degrees of separation between them.
1: Bala Bulu Corn and Brigitte Bardot were in Fagba.
2: Brigitte Bardot and Ramiro Archain were in Imota  *
3: Ramiro Archain and Shurecan Rigg were in Isheri  *
```




The util.py was adopted from
[the CS50 Search project](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/block-v1:HarvardX+CS50AI+1T2020+type@sequential+block@918082613c254e2da55e31d1894bc4be/block-v1:HarvardX+CS50AI+1T2020+type@vertical+block@d8a51672180d461d9e0a9ca02870d0d9)
