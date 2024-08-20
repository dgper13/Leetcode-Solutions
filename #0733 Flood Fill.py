from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        """
        Perform a flood fill on the image starting from the pixel at (sr, sc).

        Args:
        image (List[List[int]]): 2D grid representing the image, where each value is a color.
        sr (int): Row index of the starting pixel.
        sc (int): Column index of the starting pixel.
        new_color (int): The new color to apply.

        Returns:
        List[List[int]]: The modified image after performing the flood fill.
        """

        # If the starting pixel's color is already the new color, no need to do anything
        if image[sr][sc] != new_color:
            self.fill(image, sr, sc, image[sr][sc], new_color)
        return image

    def fill(self, image, sr: int, sc: int, color: int, new_color: int):
        """
        Recursive function to apply the new color to the current pixel and its connected neighbors.

        Args:
        image (List[List[int]]): 2D grid representing the image.
        sr (int): Current row index.
        sc (int): Current column index.
        color (int): Original color that needs to be replaced.
        new_color (int): The new color to apply.
        """

        # Check for out-of-bounds or if the current pixel is not of the target color
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != color:
            return

        # Change the current pixel's color to the new color
        image[sr][sc] = new_color

        # Recursively fill the neighboring pixels in all four directions
        self.fill(image, sr-1, sc, color, new_color)  # Up
        self.fill(image, sr+1, sc, color, new_color)  # Down
        self.fill(image, sr, sc-1, color, new_color)  # Left
        self.fill(image, sr, sc+1, color, new_color)  # Right
