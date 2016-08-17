// Agent robot_model in project tiago.mas2j

/* Initial beliefs and rules */

/* Initial goals */
!waitOrder.

/* Plans */
+!waitOrder : ended <- -ended[source(human)]; .print("ended").
+!waitOrder : goToFridge <- reset_time;-goToFridge[source(human)]; .print("fridge"); !gotoFridge. 
+!waitOrder : goToSink <- reset_time;-goToSink[source(human)];.print("sink"); !gotoSink. 
+!waitOrder : goToClean <- reset_time;+plan1; -goToClean[source(human)];.print("clean"); !gotoHuman. 
+!waitOrder : goToFeed <- reset_time;+plan2; -goToFeed[source(human)];.print("feed"); !gotoFridge. 
+!waitOrder : goToRandom <- reset_time;-goToRandom[source(human)];.print("I dont know"); !gotoRecharge. 
+!waitOrder :  not timeout <-  add_time(4); check_time(600); .print("Wait"); !waitOrder. 
+!waitOrder :  timeout <-  -timeout[source(percept)]; .print("timedout"); reset_time; !gotoRecharge.


+!gotoFridge : collision <- -collision[source(sensors)]; !gotoFridge.
+!gotoFridge : plan2 <- !gotoHuman.
+!gotoFridge : true  <- !gotoRecharge.

+!gotoSink : collision <- -collision[source(sensors)]; !gotoSink.
+!gotoSink : true <- !gotoRecharge.

+!gotoHuman : collision <- -collision[source(sensors)]; !gotoHuman.
+!gotoHuman : true & plan1 <-!gotoSink.
+!gotoHuman : true & plan2 <- !gotoRecharge.

+!gotoRecharge : collision <- -collision[source(sensors)]; !gotoRecharge.
+!gotoRecharge : true <- -plan1[source(self)]; -plan2[source(self)]; .send(human,tell,robotDone); !waitOrder.
