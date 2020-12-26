# hopalong

the code is really simple, essentially it

1. generates a grid of random points near the origin,
2. iteratively applies the transform function to it
3. plots the distribution at the end of the transformations


you can make gif by exporting an image of each frame and then use the gif() function.

play around with the a,b,c,d params to get different final images.

Its interesting to see the transient states, to do that put the plot function in the iteration (the while loop)
