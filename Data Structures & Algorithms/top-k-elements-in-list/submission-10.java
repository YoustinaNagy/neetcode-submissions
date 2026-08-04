class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        for (int num: nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        List<List<Integer>> num = new ArrayList<>();
        for (int key : map.keySet()){
            List<Integer> lst = new ArrayList<>(); 
            lst.add(key);
            lst.add(map.get(key));
            num.add(lst);
        }
        num.sort((a, b) -> Integer.compare(b.get(1), a.get(1)));
        
        int[] res = new int[k];
        for (int i=0; i<k;i++){
            res[i]= num.get(i).get(0);
        }
        return res;
    }
}
