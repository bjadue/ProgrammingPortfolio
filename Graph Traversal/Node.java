package Graph;

import java.util.LinkedList;
public class Node {
    //basics
    public String name;
    public LinkedList<Edge> edges; //adjacency list

    //PRIMS
    public boolean visited;
    public int distance;
    public Node prev;

    //
    public double lat, lng;

    //todo more to come

    public Node(String name){
        this.name = name;
        edges = new LinkedList<>();

    }

    //def __str__(self):
    public String toString(){
        return this.name;
    }
}
