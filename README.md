SpaceX Demo
===========
This demo displays SpaceX launch information, fetched from the SpaceX API.

## Running the Demo

To run the demo, you will need a docker-compose version that supports compose file format version 2+. To run the demo, simply:

```cd docker/compose; docker-compose up```

On your first run, this will build a minimal image with the full demo and initialize the database with data from the SpaceX API. Once started, the demo will be available on port `9090`. Enter a search term to see matching results.

The demo uses a simple Flask API backed by MongoDB, with Vue.js on the frontend. To query the API directly, the following endpoints are available:

```/api/v1/launches```
```/api/v1/launch/<int:flight_number>```

The `launches` endpoint can be filtered by passing a query parameter `q` with the value to search for. This will perform a substring search of the following fields:

* `launch_year`
* `rocket.rocket_name`
* `rocket.rocket_type`
* `launch_site.site_name`

For example, a query for "kwaj" will return all launches from Kwajalein Atoll.
