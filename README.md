# ProjectMongo

In this project I had to select the offices location for an office according to some conditions. The geographic point I have selected is with longitude:-122.333359, latitude:47.603364 in the city of Seattle.

The conditions I have accomplished are the following, because around 500 metres there is:
1. 9 vegan restaurants for the CEO.
2. 8 starbucks for the accountants.
3. 7 nightclubs for the party of the workers.
4. 1 kindergarten for the children of the workers.

In order to achieve the solution, I had to import with pymongo the collection companies with a Mongo query and clean the database with pandas. Then to upload the geo_json index to Mongo I had to make the getLocation function.

Then I made all the requests to the Google Places API to find the starbucks, vegan restaurants, nightclubs and kindergarten that were around the coordinates of the companies I had, and then uploaded as new collections to Mongodb. 

After that I had to make the geoqueries to see the quantity of facilities that were around the companies in a radius of 500 metres, and rank the companies according to that matter.

The final step was to display the location of the top 3 companies according to the previous ranking and as the three companies where in the same neighbourhood I have selected the first one to put the offices in the plant above of their offices.

The solution can be seen in the image "solution.png" in the output folder.