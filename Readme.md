# Open Door Take Home Problem: Software Engineer

## The API endpoint
[API endpoint link](https://arcane-sands-4838.herokuapp.com/listings?)

## What I would do next
The following changes are made with the assumption that I am the client:
* Prettify the output (it's currently proper GeoJSON, but not very easy on the eyes. Put in newlines in the GeoJSON output as is convention.
* Have a consumer-facing end where the houses are points on a map and are selectable (all selected points have more information viewed below). \n
* Warnings on certain parameters not being proper parameters (currently they're silently ignored)
* Proper introduction to the API at /listings instead of a all of the houses (no conditions = they all meet the condition)
* Efficient way of handling larger data sets (sending 5 GB of housing data at once with a browser isn't smart). 
* Geographic parameters (lat/lon coordinates forming a square, houses within that square are returned subject to the other conditions)
