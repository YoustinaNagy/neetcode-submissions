class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=s.length()){
            return false;
        }
        Map<Character,Integer> maps = new HashMap<>();
        Map<Character,Integer> mapt = new HashMap<>();

        for(char c : s.toCharArray()){
            maps.put(c, maps.getOrDefault(c,0)+1);
        }
        for(char c : t.toCharArray()){
            if(maps.containsKey(c)==false){
                return false;
            }
            mapt.put(c, mapt.getOrDefault(c,0)+1);
        }
        if(maps.size()!=mapt.size()){
            return false;
        }
        for (Character key : maps.keySet()) {
            if(mapt.containsKey(key)==false){
                return false;
            }
            if(!maps.get(key).equals(mapt.get(key))) {

                // System.out.println(key  + " s="+maps.get(key) +" t="+ mapt.get(key));
                // System.out.println(maps.get(key)!=mapt.get(key));
                return false;
            }
        }

        return true;
    }
}
