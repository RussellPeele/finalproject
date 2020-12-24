Perfect South Park Episode

Jeremiah McClure came up with the idea for an application that chooses the ideal South Park Episode
based on the viewers current mood. It occurred to me that while southpark.cc.com has a random episode
generator, they do not narrow the search in any way. Using our new python, html, and css skills, and
little linear algebra we built a website that picks your perfect episode based on how you feel right now.

We created a spreadsheet of episodes and crowd sourced with South Park fans ratings for episode attributes.
Then we stored the ratings as a csv file that could then be read by our application in an episode matrix.
Each row vector then represents an episode.

The user preferences are selected via dropdown menus on the site and then stored as the “human” vector.
The human vector is subtracted from each row vector, and the magnitude of all the difference is calculated.
The smallest magnitude is considered the best fit and gives us the position of the perfect episode. At this
point the application redirects to the perfect episode wikipedia page.

After watching, the human is encouraged to rate their experience such that our algorithm can learn.
If the episode did not fulfill their heart’s desire, the application then modifies the episode matrix to more
appropriately rate that episode’s attributes.


