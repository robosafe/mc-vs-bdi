// Agent dog in project tiago.mas2j

/* Initial beliefs and rules */

/* Initial goals */
!setup.

/* Plans */

+!setup : true <- .random(X); !action.

+!action : X >= 0.5 <- .send(sensors,tell,noDogCollision); !setup. 
+!action : X < 0.5 <- .send(sensors,tell,dogCollision); !setup. 
