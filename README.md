
### **Background**

The *Six Degrees of Kevin Bacon game*, shows how any two actors in Hollywood can be connected within just six steps;
where each step consists of finding a film both starred in.
In this problem, I implemented Six degrees in finding the connections between any two suspects by choosing a sequence of crimes scenes that connects them.

I frame this as a search problem
- The *states* being the different people iterated over
- The *intial state* is defined by the first person(source)
- the *goal* is the target suspect
Using BFS(breadth-first-search), the shortest path(connection) from one suspect to another can be found 


***Utility functions***

The *main function* is implemented as a test/driver
- loads the data from directory into memory 
- prompts the user to type in the two names(source & target)

The *person_id_for_name* function 
- retrieves the id for any person
The *shortest_path* function, 
- finds and returns the shortest path link betweent the *source* and the *target* 

The util.py was adopted from [the CS50 Search project](https://learning.edx.org/course/course-v1:HarvardX+CS50AI+1T2020/block-v1:HarvardX+CS50AI+1T2020+type@sequential+block@918082613c254e2da55e31d1894bc4be/block-v1:HarvardX+CS50AI+1T2020+type@vertical+block@d8a51672180d461d9e0a9ca02870d0d9)
