import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class SymmetricOrder {
    
    public static String[] clownSort(String[] unsorted){
        
        ArrayList<String> list1 = new ArrayList<String>();
        ArrayList<String> list2 = new ArrayList<String>();
        boolean alt = true;
       
        for(int i = 0; i < unsorted.length; i++){
            if(alt){
                alt = false;
                list1.add(unsorted[i]);
            }
            else{
                alt = true;
                list2.add(unsorted[i]);
            }
        } 
    
        Collections.reverse(list2);
        list1.addAll(list2);
       
        String[] sorted = new String[list1.size()];
        list1.toArray(sorted);
        
        return sorted;
    } 
    
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int number = Integer.parseInt(reader.nextLine());
        
        ArrayList<String[]> MasterList = new ArrayList<String[]>();
        
        while(number != 0){
            String[] input = new String[number];
            
            for(int i = 0; i < number; i++){
                input[i] = reader.nextLine();
            } 

            MasterList.add(clownSort(input));
            number = Integer.parseInt(reader.nextLine());
        } 
          
        for(int m = 0; m < MasterList.size(); m++){
            System.out.println("SET " + (m+1));
            for(int i = 0; i < MasterList.get(m).length; i++){
                System.out.println(MasterList.get(m)[i]);
            }
        }      
    } 
}