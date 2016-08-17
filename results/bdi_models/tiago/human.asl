// Agent human in project tiago.mas2j

/* Initial beliefs and rules */

/* Initial goals */
!setup.

/* Plans */

+!setup : meta <- !activate.
+!setup : true <- !setup.

+!activate : fridge <- -meta[source(meta)]; -fridge[source(percept)];.print("Fridge"); .send(robot_code,tell,goToFridge); tofile("fridge"); !waiting.
+!activate : sink <- -meta[source(meta)]; -sink[source(percept)]; .print("Sink"); .send(robot_code,tell,goToSink); tofile("sink"); !waiting.
+!activate : feed <- -meta[source(meta)];-feed[source(percept)]; .print("Feed"); .send(robot_code,tell,goToFeed); tofile("feed"); !waiting.
+!activate : clean <- -meta[source(meta)];-clean[source(percept)]; .print("Clean"); .send(robot_code,tell,goToClean); tofile("clean"); !waiting.
+!activate : random <- -meta[source(meta)]; -random[source(percept)]; .print("Random"); .send(robot_code,tell,goToRandom); tofile("whatever"); !waiting.
+!activate : true <- .print("Ended"); .send(robot_code,tell,ended). 

+!waiting: not robotDone <-.print("Waiting");!waiting.
+!waiting: robotDone <- -robotDone[source(robot_code)]; !activate.

