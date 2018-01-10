class Solution(object):
    
    def visit(self, i,j,pos_c,new_c,image, seen):
        if 0<=i<len(image) and 0<=j<len(image[0]) and image[i][j] == pos_c and (i,j) not in seen:
            seen.add((i,j))
            image[i][j] = new_c
            self.visit(i+1, j, pos_c, new_c, image, seen)
            self.visit(i-1, j, pos_c, new_c, image, seen)
            self.visit(i, j+1, pos_c, new_c, image, seen)
            self.visit(i, j-1, pos_c, new_c, image, seen)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        seen = set()
        pos_c = image[sr][sc]
        self.visit(sr,sc,pos_c,newColor,image, seen)
        return image
        
