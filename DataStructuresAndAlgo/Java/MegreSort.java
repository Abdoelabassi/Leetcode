import java.util.ArrayList;

public class MegreSort {

    public static void main(String[] args){

    }

    public static ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b){
        int i, j = 0;
        ArrayList<Integer> merged_list = new ArrayList<Integer>();
        while (i < a.size() && j < b.size()){
                if (a.get(i) < b.get(j)){
                    merged_list.add(a.get(i));
                    i += 1;
                }else{
                    merged_list.add(b.get(j));
                    j += 1;
                }
        }
        while (i < a.size()){
            merged_list.add(a.get(i));
            i += 1;
        }
        while (j < b.size()){
            merged_list.add(b.get(j));
            j += 1;
        }

        return merged_list;
    }

    public static ArrayList<Integer> merge_sort(ArrayList<Integer> a){
        if (a.size() == 1){
            return a;
        }
        int mid = (a.size() / 2);
    }

}