# Java-Class-Finder
Created : January 2017

This is a relatively simple script that finds all the classes in the JDK source files. I wrote this one night while procrastinating doing my homework. My Mobile Applications professor posed the question in class and it sparked my interest. The script recursively searches through the directory specified in the arg, finding all the private/public classes and interfaces, both top-level and nested. My regex syntax might be a bit off, but I believe it to be accurate based on data found [here](http://stackoverflow.com/questions/3112882/how-many-classes-are-there-in-java-standard-edition). 

In order to prep the data, I simply extracted both the "Java/JDK/javafx-src.zip" and "Java/JDK/src.zip" to a seperate directory and searched from there. As of Java version 1.8.0_102, I found 8180 classes. 
