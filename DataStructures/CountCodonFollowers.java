//Jacob Siepker
//CSC 301
//5.24.2020

package symboltable;

import algs4.StdIn;
import algs4.StdOut;
import myalgs4.SeparateChainingHashST;
import algs4.Queue;

public class CountCodonFollowers {

	public static void main(String[] args) {
		
		//Change string here to change RNA input file
		String RNAReadFile = "data/SARSCoV2-S-gene-WH.txt";
		
		String[] allCodons = new String[64];
		
		StdIn.fromFile("data/codonlist.txt"); //reads in file for list of codons
		
		for (int i = 0; i < 64; i++) { //for each of the 64 codon types, put into allCodons[]
			String text = StdIn.readLine();
			allCodons[i] = text;
		}
		
		StdIn.fromFile(RNAReadFile);
		String RNAFile = StdIn.readAll();  //saves read file as string
		SeparateChainingHashST<String, Queue<Integer>> locations = new SeparateChainingHashST<>(); //ST for codon locations

		for (int i = 0; i < RNAFile.length(); i+=3) { //runs through read file, adds new key and queue or updates queue to include all locations of codon
			String thisCodon = RNAFile.substring(i, i+3);
			if (locations.contains(thisCodon)) {
				locations.get(thisCodon).enqueue(i);
			}
			else {
				Queue<Integer> temp = new Queue<>();
				temp.enqueue(i);
				locations.put(thisCodon, temp);
			}
		}
		
		//Rest is based on pseudo-code from assignment file
		StdOut.println("Number of different codons following each codon");
		for (String thisCodon: allCodons) {  //for each codon
			StdOut.print(thisCodon + ": ");
			if (locations.contains(thisCodon)){ //if it exists in the locations ST
				SeparateChainingHashST<String, Boolean> thisCodonFollowers = new SeparateChainingHashST<>(); //creates new ST
				
				for (Integer loc: locations.get(thisCodon)) { //for each location in the locations queue
					if (loc < RNAFile.length()-3) {	//guard to avoid array index error
						String nextCodon = RNAFile.substring(loc+3, loc+6); //get next codon
						thisCodonFollowers.put(nextCodon, true); //put next codon into the new ST
					}
				}
				
				StdOut.println(thisCodonFollowers.size()); //print number of codons that follow this codon
			}
			else { //if codon does not exist in the locations ST
				StdOut.println("Does not occur in the sequence");
			}
		}
		
	}

}
