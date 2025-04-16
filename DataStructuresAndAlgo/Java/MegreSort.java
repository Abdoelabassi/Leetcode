import java.util.ArrayList;

public class MegreSort {

    public static void main(String[] args){

        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(5);
        list.add(2);
        list.add(9);
        list.add(1);
        list.add(3);
        list.add(4);
        list.add(8);
        list.add(7);
        list.add(6);

        System.out.println("Unsorted List: " + list);
        ArrayList<Integer> sorted_list = merge_sort(list);
        System.out.println("Sorted List: " + sorted_list);

    }

    public static ArrayList<Integer> merge(ArrayList<Integer> a, ArrayList<Integer> b){
        int i = 0, j = 0;
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
        ArrayList<Integer> first_half = new ArrayList<Integer>(a.subList(0, mid));
        ArrayList<Integer> second_half = new ArrayList<Integer>(a.subList(mid, a.size()));
        first_half = merge_sort(first_half);
        second_half = merge_sort(second_half);
        return merge(first_half, second_half);
    }

}