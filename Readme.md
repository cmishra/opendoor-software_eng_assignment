# Open Door Take Home Problem: Software Engineer

## The API endpoint
[API endpoint link](https://arcane-sands-4838.herokuapp.com/listings?)

## What I would do next
The following changes are made with the assumption that I am the client. Order does not indicate priority.
* Prettify the output (it's currently proper GeoJSON, but not very easy on the eyes). Put in newlines in the GeoJSON output as is convention.
* Have a consumer-facing end where the houses are points on a map and are selectable. All selected points have more information about them pop up below the map. 
* Warnings on certain parameters not being proper parameters (currently they're silently ignored). i.e. if someone says "maxprice" instead of "max_price", right now I just ignore the condition. I would like to tell them "warning: 'maxprice' not a valid parameter" 
* Proper introduction to the API at /listings instead of all of the houses being returned (no conditions = they all meet the condition)
* Efficient, fault-tolerant way of handling larger data sets (sending 5 GB of housing data at once with a browser isn't smart). 
* Geographic parameters (lat/lon coordinates forming a square, houses within that square are returned subject to the other conditions)
