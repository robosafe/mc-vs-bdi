// Agent sensing in project tiago.mas2j

/* Initial beliefs and rules */
noDogCollision.

/* Initial goals */
!sense. 

/* Plans */
+!sense : dogCollision <- -dogCollision[source(dog)]; .print("collision"); .send(robot_code,tell,collision); !sense.
+!sense : noDogCollision <- -noDogCollision[source(dog)]; -noDogCollision[source(self)]; .print("no collision"); !sense. 
+!sense : true <- !sense. 
