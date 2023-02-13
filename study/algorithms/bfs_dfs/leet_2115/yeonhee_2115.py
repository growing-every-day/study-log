import collections

# 675 ms, 17mb
class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        ans = []
        supplies = set(supplies)
        graph = collections.defaultdict(list)
        inDegree = collections.Counter()
        q = collections.deque()

        # Build graph
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    graph[ingredient].append(recipe)
                    inDegree[recipe] += 1

        # Topology
        for recipe in recipes:
            if inDegree[recipe] == 0:
                q.append(recipe)

        while q:
            u = q.popleft()
            ans.append(u)
            for v in graph[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)

        return ans
    
s = Solution()
print(s.findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))