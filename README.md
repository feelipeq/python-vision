# Image-Labelist

Get Vision Label from Images and Upload to Drive
---

Application that get google vision labels and texts of an image and upoad it to Google Drive with those labels.

How to use:
- Define the Destination folder to search for images

You can see the performance of the uploads on Elasticsearch

Stack
---

- Python
- Elasticsearch
- Google Vision API
- Google Cloud

# Tasks
## Tasks completed
- [x] Recursively search for images in any filesystem;
- [x] Integrate with Google Cloud Vision API;
- [x] Integrate with Google Drive;
- [x] Upload images to Drive with Vision Labels;
- [x] Elasticsearch monitoring (Integrations response time)
- [x] Translate google vision labels

## Tasks to do
- [ ] Develop Web Interface for Single Images update
- [ ] Use simple_settings to manage Application properties
- [ ] Test plan

## Requirements

- Python 3

## Installing

- Is recommend the use of [virtualenv](https://virtualenv.pypa.io/) to manage Python enviroment
- Install the requirements:

    `make install`


# Makefile
## Essentials commands:
```
Commmands:           Descriptions:

run                 Starts the App
```

## Development Options
* `make install`<br/>
    * Install all dependencies of project<br/>
* `make run`<br/>
    * Start the application `<br/>
* `make format`<br/>
    * Formats the Code`<br/>


# Application Diagram

## Application Functions

![](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=dGl0bGUgSW1hZ2VzIERldGVjdGlvbgoKQXBwbGljYXRpb24tPkZpbGVTeXN0ZW06IFNlYXJjaCBmb3IAMAYocykKABYKLT4ALgs6IFJldHVybgAgCSBQYXRoAE0OR0MgVmlzaW9uIEFQSTogU2VuZACBBwcKAA4NAEQVcyBMYWJlbHMgYW5kIFRleHRzAIEqD0dDIFRyYW5zbGF0ZQBcBQAECgBvBwA7BgoAGRAAgToOAIFAB2xhYmVsAEcKZABdEG9vZ2xlIERyaXZlAIFEBnMAglMGIHdpdGgAYggKCg&s=modern-blue)









### Environment variables

- DEBUG
- DATABASES_DEFAULT_URI
- DEFAULT_PRICING_CALL_CHARGE
- DEFAULT_PRICING_TARIFF
- DEFAULT_PRICING_BACKEND
- DEFAULT_NOTIFICATION_BACKEND
- DEFAULT_STORAGE_BACKEND
- IS_ENABLE_TO_ENQUEUE_REPORT_BILL
