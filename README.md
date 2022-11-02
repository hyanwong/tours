Insert a tour into the OneZoom database with:

```
curl -X PUT -H "Content-Type: application/json" --user admin \
    http://.../tour/data.json/edge_species \
    -d @edge_species.json
```

Once uploaded you can trigger a tour manually in the javascript console with:

```
onezoom.controller.tour_start('/tour/data.html/edge_species')
```
