class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> map = new HashMap<>();
        int l=0;
        int r=0;
        int res=0;
        while (r<s.length()){
            map.put(s.charAt(r), map.getOrDefault(s.charAt(r), 0) + 1);
            int maxValue = Collections.max(map.values());
            int window = r-l+1 ;
            if (window - maxValue <= k){
                res= Math.max(res,window);
                r++;
            }else{
                map.put(s.charAt(l), map.get(s.charAt(l)) -1);
                l++;
                r++;
            }
        }
        return res;
    }
}
