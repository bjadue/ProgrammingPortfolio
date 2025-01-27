package Graph;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class WarnerDemoDat {
    public static void main(String[] args) throws Exception{
        //read
        File file = new File("map.dat");
        Scanner f = new Scanner(file);

        int numNodes = Integer.parseInt(f.nextLine());
        System.out.println(numNodes);
        Node[] nodes = new Node[numNodes];
        Graph g = new Graph();

        for(int i = 0; i < numNodes; i++){
            //System.out.println(f.nextLine());
            String[] tokens = f.nextLine().split(",");

            System.out.println(tokens[0]);
            System.out.println(tokens[1]);
            System.out.println(tokens[2]);

            Node tmp = new Node(tokens[4]);
            tmp.lat = Double.parseDouble(tokens[1]);
            tmp.lng = Double.parseDouble(tokens[2]);
            //store the jawn
            nodes[i] = tmp;
            // place to graph
            g.addNode(tmp);
        }

        //System.out.println(nodes[0]);

        int numEdges = Integer.parseInt(f.nextLine());

        for(int i = 0; i < numEdges; i++){
            //add edges
            String[] tokens = f.nextLine().split(" ");

            int from = Integer.parseInt(tokens[0]);
            int to = Integer.parseInt(tokens[1]);
            int dir = Integer.parseInt(tokens[2]);

            final int SCALE = 10000;
            double w = haversine(nodes[from].lat, nodes[from].lng, nodes[to].lat, nodes[to].lng);
            int scaled_w = (int) (SCALE * w);
            System.out.println(w);

            if(dir == 2){
                g.addEdge(nodes[from], nodes[to], scaled_w);
                g.addEdge(nodes[to], nodes[from], scaled_w);
            }else{
                g.addEdge(nodes[from], nodes[to], scaled_w);
            }
            
        }

        g.print();

        g.dijkstra(nodes[17], nodes[2]);

        
        //create

        //add

        f.close();
    }

    static double haversine(double lat1, double lon1,
            double lat2, double lon2) {
        // distance between latitudes and longitudes
        double dLat = Math.toRadians(lat2 - lat1);
        double dLon = Math.toRadians(lon2 - lon1);

        // convert to radians
        lat1 = Math.toRadians(lat1);
        lat2 = Math.toRadians(lat2);

        // apply formulae
        double a = Math.pow(Math.sin(dLat / 2), 2) +
                Math.pow(Math.sin(dLon / 2), 2) *
                        Math.cos(lat1) *
                        Math.cos(lat2);
        double rad = 6371;
        double c = 2 * Math.asin(Math.sqrt(a));
        return rad * c;
    }
}
