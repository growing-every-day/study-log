from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int) # 

        for recipe, ingredient in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient)

            for ing in ingredient:
                graph[ing].append(recipe)

        ans = []
        
        queue = deque(supplies)
        recipes = set(recipes)

        while queue:
            supply = queue.popleft()

            if supply in recipes:
                ans.append(supply)
            
            for recipie in graph[supply]:
                indegree[recipie] -= 1

                if indegree[recipie] == 0:
                    queue.append(recipie)

        return ans