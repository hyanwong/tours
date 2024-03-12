# OneZoom Tours

Tour JSON documents that can be inserted into an instance's database.

The JSON format is described in https://github.com/OneZoom/OZtree/blob/main/controllers/tour.py

## Uploading tours

You can insert a single tour or multiple tours into a OneZoom instance with the ``upload.py`` script:

```
./upload.py http://localhost:8000/ *.json
```

You can also use CURL directly:

```
curl -X PUT -H "Content-Type: application/json" --user admin \
    http://localhost:8000/tour/data.json/edge_species \
    -d @edge_species.json
```

Fetch it back again with:

```
curl http://localhost:8000/tour/data.json/edge_species
```

Or as HTML with:

```
curl http://localhost:8000/tour/data.html/edge_species
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

## Creating a user to add tours via.

See the [Creating auth users & groups section of README.markdown](https://github.com/OneZoom/OZtree#creating-auth-users--groups)

Summary being:

* Specify an admin password on web2py startup with ``-a pass``
* Go to /appadmin/insert/db/auth_user
* Enter at least a first & last name, username & password

Then use the username / password with the curl command above.

## Other documentation

* HTML tour syntax (what the JSON is converted to): https://github.com/OneZoom/OZtree/blob/main/OZprivate/rawJS/OZTreeModule/src/tour/Tour.js
* Extended HTML tour syntax in the relevant handler plugins: https://github.com/OneZoom/OZtree/tree/main/OZprivate/rawJS/OZTreeModule/src/tour/handler
* Pinpoints describing locations on the tree: https://github.com/OneZoom/OZtree/blob/main/OZprivate/rawJS/OZTreeModule/src/navigation/pinpoint.js
* URLs, including all attributes that can be set in the querystring: https://github.com/OneZoom/OZtree/blob/main/OZprivate/rawJS/OZTreeModule/src/navigation/state.js
* Additional documentation on highlights: https://github.com/OneZoom/OZtree/blob/main/OZprivate/rawJS/OZTreeModule/src/projection/highlight/highlight.js
