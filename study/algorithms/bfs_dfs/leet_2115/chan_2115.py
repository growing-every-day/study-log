from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list) # key: ingredient, value: recipe
        indegree = defaultdict(int) # key: recipe, value: ingredient count

        # graph, indegree 초기화
        for recipe, ingredient in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient)

            for ing in ingredient:
                graph[ing].append(recipe)

        ans = []
        
        queue = deque(supplies)
        recipes = set(recipes)


        while queue:
            supply = queue.popleft()

            # supply가 recipe에 포함되어 있으면 ans에 추가
            if supply in recipes:
                ans.append(supply)
            
            # supply가 ingredient에 포함되어 있으면 recipe indegree 감소
            for recipie in graph[supply]:
                indegree[recipie] -= 1

                if indegree[recipie] == 0:
                    queue.append(recipie)

        return ans