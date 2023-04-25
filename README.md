# OneZoom Tours

Tour JSON documents that can be inserted into an instance's database.

The JSON format is described in https://github.com/OneZoom/OZtree/blob/main/controllers/tour.py

## Inserting a tour

Insert a tour into the OneZoom database with:

```
curl -X PUT -H "Content-Type: application/json" --user admin \
    http://.../tour/data.json/edge_species \
    -d @edge_species.json
```

## Playing a tour

Once uploaded you can trigger a tour manually in the javascript console with:

```
onezoom.controller.tour_start('/tour/data.html/edge_species')
```

Or trigger it on load (although be warned that autoplaying will not trigger before a click):

```
/life?tour=/tour/data.html/superpowers
```
