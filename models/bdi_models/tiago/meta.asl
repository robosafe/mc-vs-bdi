// Agent meta in project tiago.mas2j

/* Initial beliefs and rules */

/* Initial goals */
!setup.

/* Plans */
+!setup : true <- get_beliefs; .send(human,tell,meta).

