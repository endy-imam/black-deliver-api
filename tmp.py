from deliver.models import Restaurant

DYNAMO_TMP = {
    "id": "4e935397-848c-488b-b3e2-bb933b5c2064",
    "name": "Felix BBQ with Soul",
    "latitude": 33.20989,
    "longitude": -117.31234,
    "address": "3616 Ocean Ranch Blvd, Oceanside, CA 92056",
    "menuUrl": "https://www.felixsbbq.com/",
    "pickupAvailable": True,
    "deliveryAvailable": True,
    "services": {
        "website": {
            "url": "https://www.felixsbbq.com/",
            "pickup": True,
            "delivery": True
        },
        "apps": {
            "Grubhub": {
                "url": "https://www.grubhub.com/",
                "pickup": True,
                "delivery": True
            },
            "Doordash": {
                "url": "https://www.doordash.com/",
                "pickup": True,
                "delivery": True
            },
            "Postmates": {
                "url": "https://postmates.com/merchant/",
                "pickup": True,
                "delivery": True
            }
        }
    }
}
