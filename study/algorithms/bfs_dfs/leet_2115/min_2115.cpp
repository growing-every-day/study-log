class Solution {
public:

    bool DFS(map<string, vector<string>> mp, set<string> &set, map<string, bool> &visited, string recipe){
        visited[recipe] = true;
        bool canMake = true;
        for (auto x : mp[recipe]){
            if (set.find(x) == set.end()){
                if (visited.find(x) != visited.end() && !visited[x]){
                    canMake = canMake && DFS(mp, set, visited, x);
                }
                else{
                    return false;
                }
            }
        }
        if (canMake){
            set.insert(recipe);
        }
        return canMake;
    }

    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        vector<string> answer;
        set<string>set(supplies.begin(), supplies.end());
        map<string, vector<string>> mp;
        map<string, bool> visited;
        
        for (int i = 0; i < recipes.size(); i++){
            mp[recipes[i]] = ingredients[i];
            visited[recipes[i]] = false;
        }

        for (int i = 0; i < recipes.size(); i++){
            string recipe = recipes[i];
            bool canMake = false;
            if (visited[recipe] == false){
                canMake = DFS(mp, set, visited, recipe);
                if (canMake == true){
                    answer.push_back(recipe);
                }
            }
            else if(visited[recipe] == true && set.find(recipe) != set.end()){
                answer.push_back(recipe);
            }
        }
        return answer;
    }
};
