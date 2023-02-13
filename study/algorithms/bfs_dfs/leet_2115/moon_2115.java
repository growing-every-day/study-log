// Runtime : 57ms, Memory : 45.3MB
class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        Map<String, List<Integer>> map = new HashMap<>();
        int[] ingredientCount = new int[recipes.length];

        for(int i=0; i<recipes.length; i++){
            for(String ingredient : ingredients.get(i)){
                map.putIfAbsent(ingredient, new ArrayList<>());
                map.get(ingredient).add(i);
                ingredientCount[i]++;
            }          
        }    

        List<String> answer = new ArrayList<>();
        Queue<String> queue = new ArrayDeque<>();

        for(String supply : supplies){
            queue.add(supply);
        }

        while(!queue.isEmpty()){
            String cur = queue.poll();

            if(!map.containsKey(cur)){
                continue;
            }

            for(int value : map.get(cur)){
                ingredientCount[value]--;
                if(ingredientCount[value]==0){
                    queue.add(recipes[value]);
                    answer.add(recipes[value]);
                }
            }
        }

        return answer;
        
    }
  public static void main(String[] args){
  
  }
}
