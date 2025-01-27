package Graph;

import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class Graph {
    //balls
    LinkedList<Node> nodes;
    private final boolean DEBUG = true;

    public Graph(){
        nodes = new LinkedList<>();
    }

    /**
     * Add a vertex to the graph.
     */
    public boolean addNode(Node v){
        return nodes.add(v);
    }

    public boolean addEdge(Node from, Node to, int weight){
        return from.edges.add( new Edge(from, to, weight) );
    }

    public void print(){
        // for node n in nodes
        // for e in list:
        for(Node n : nodes){
            for(Edge e : n.edges){
                System.out.println(e);
            }
            System.out.println("");
        }    
    }
    //Modified print function to print the path in node ID.

    public void prim(){
        if(DEBUG)System.out.println("Operating prims");
        int mst_weight = 0;

        //make sure all nodes are unvisited/unprocessed
        unvisitAllNodes();
        if(DEBUG)System.out.println("Unvisit all nodes");

        //start anywhere get free wifi anywhere you gooooo
        Node tmp_node = nodes.getFirst(); //not a removal :(
        tmp_node.visited = true;

        while(!allNodesVisited()){
            // do stuff while allNodesVisited is false
            // find smollest edge har har
            Edge tmp_edge = findSmallestWeight();
            if(DEBUG)System.out.println("\nSmallest edge selected: " + tmp_edge);

            //add up mst cost
            mst_weight += tmp_edge.weight;
            if(DEBUG)System.out.println("Cost so far: " + mst_weight);

            //mark node at end of edge as visited
            tmp_edge.end.visited = true;
            if(DEBUG)System.out.println("Marked destination as visited.\n");
        }

        System.out.println("MST total cost: " + mst_weight);
    }

    /**
     * Dijkstra's- get path with minimal cost from start to end
     */
    public void dijkstra(Node start, Node end){
        //init
        unvisitAllNodes(); //set all visited bools to false
        resetDistanceData();

        Node curr = start;
        curr.distance = 0;

        
        Scanner k = new Scanner(System.in); //input("")
        

        while(curr != null){
            p("Current Node is " + curr);

            if(curr == end){
                break;
            }

            //process all edges
            for(int i = 0; i < curr.edges.size(); i++){
                Edge e = curr.edges.get(i);
                if(DEBUG)p("Edge " + (i + 1) + " " + e + " visited? " + e.end.visited);

                if(e.end.visited){
                    continue;//pass
                }

                int newDistance = curr.distance + e.weight;
                if(DEBUG)p("\t\t newDistance=" + newDistance);

                if(DEBUG)p("\t\tnewDistance= < e.end.distance " + newDistance + " < " + e.end.distance);

                if(newDistance < e.end.distance){
                    p("\t\tSmaller distance found.");
                    e.end.distance = newDistance;
                    e.end.prev = curr;
                }
            }//done proc edges

            curr.visited = true;

            curr = findSmallestWeightUnvisited();
            if(DEBUG)p("curr is now " + curr);
            if(DEBUG)k.nextLine(); //wait for enter key

        }

        //Print the path...

        Stack<Node> path = new Stack<>();
        curr = end;
        while(curr != null){
            path.push(curr);
            curr = curr.prev;
            //unload all nodes onto stack in reverse
        }

        while(!path.isEmpty()){
            Node n = path.pop();
            p(n + " (" + n.distance + ")");
            //concatinate to convert to a string (long live java)
        }
        
    }

    private Node findSmallestWeightUnvisited(){
        int min = Integer.MAX_VALUE;
        Node candidate = null;

        for(Node n : nodes){
            //Short-circuit (LIKE THE MOVIE RAAAAAAAAAAAAAAAAAAAAAAAAAAH o_o)
            if(!n.visited && n.distance < min){
                    min = n.distance;
                    candidate = n;
            }
        }
        return candidate;
    }

    private void p(String s){
        System.out.println(s);
    }

    private void resetDistanceData(){
        for(Node n : nodes){
            n.distance = Integer.MAX_VALUE -1;
        }
    }


    //the meat of prims
    private Edge findSmallestWeight(){
        int min = Integer.MAX_VALUE;
        Edge candidate = null;

        for(Node n : nodes){
            if(n.visited){
                if(DEBUG)System.out.println("pardon me");
                if(DEBUG)System.out.println("Checked node " + n);
                for(Edge e : n.edges){
                    if(e.weight < min && !e.end.visited){
                        min = e.weight;
                        candidate = e;
                        //will find smallest number, then update candidate to be that node
                    }
                }
            }
        }

        return candidate;
    }

    private boolean allNodesVisited(){
        for(Node n : nodes){
            if(n.visited == false){
                return false;
            }
        }
        //end early if false found, otherwise end with true
        return true;
    }

    private void unvisitAllNodes(){
        for(Node n : nodes){
            n.visited = false;
        }
    }
}
