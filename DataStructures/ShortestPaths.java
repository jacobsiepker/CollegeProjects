//Jacob Siepker
//CSC 301
//6.1.2020

package Graphs;

import algs4.BreadthFirstPaths;
import algs4.Graph;
import algs4.StdIn;
import algs4.StdOut;

public class ShortestPaths {

	public static void main(String[] args) {
		//Read Files
		String VertNum = "data/VertexNumbers.txt";
		String Edges = "data/Edges.txt";
		String PathQuery = "data/PathQuery.txt";
		
		StdIn.fromFile(VertNum);
		int n = 0; 
		
		while (StdIn.readLine() != null) {
			n++; //counts one for each line in vertex id file
		}
		
		Graph G = new Graph(n); //creates new graph
		
		StdIn.fromFile(Edges); //open edges file
		Boolean end = false;  //creates exit boolean
		while (end != true) {
			String EdgePair = StdIn.readLine(); 
			if (EdgePair == null) { //validates for text
				end = true;
				break;
			}
			String[] edges = EdgePair.split(" "); //split text in 2 parts
			G.addEdge(Integer.parseInt(edges[0]), Integer.parseInt(edges[1])); //add each vert as edge
		}
		
		
		StdIn.fromFile(PathQuery); //open path query file
		end = false;
		
		while(end != true) {
			String currQuery = StdIn.readLine(); //for each line in path query file
			if(currQuery == null) {
				end = true;
				break;
			}
			String[] currQueryA = currQuery.split(" "); //splits into 2 parts, u v
			
			BreadthFirstPaths currPath = new BreadthFirstPaths(G,Integer.parseInt(currQueryA[0]));
			StdOut.print(Integer.parseInt(currQueryA[0]) + " connected to " + Integer.parseInt(currQueryA[1]) + "?"); //Output for rest
			if(currPath.hasPathTo(Integer.parseInt(currQueryA[1]))) {
				StdOut.print(" Yes, by the path ");
				for (Integer paths: currPath.pathTo(Integer.parseInt(currQueryA[1]))) {
					StdOut.print(paths + "-");
				}
				StdOut.println("");
			}
			
			else {
				StdOut.println(" No!");
			}
		}
		
	}

}
