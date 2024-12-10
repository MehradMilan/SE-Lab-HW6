for i in {1..10}; do curl -X POST -H "Content-Type: application/json"     -d '{"name": "Item'$i'", "value": '$i'}' http://localhost:8001/items; done
curl http://localhost:8001/items
