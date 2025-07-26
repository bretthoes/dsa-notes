from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # type
        # sorting, binary search
        # approach:
        # sort the products list, 
        result = []
        products.sort()
        buildingSearch = ""
        for char in searchWord:
            currentResult = []
            buildingSearch += char
            # at each search char
            # use binary sort to get lowest lexographical match
            
            low = 0
            high = len(products) - 1
            found = 0
            while low < high:
                mid = (low + high) // 2
                if buildingSearch < products[mid]:
                    high = mid
                    found = mid
                elif buildingSearch > products[mid]:
                    low = mid + 1
                else:
                    # found
                    found = mid
                    break
            
            # check next 3 indexes from here, include if valid
            while len(currentResult) < 3 and found < len(products) and products[found].startswith(buildingSearch):
                currentResult.append(products[found])
                found += 1
            result.append(currentResult)

        return result
            


        
