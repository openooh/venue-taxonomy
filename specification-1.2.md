# Digital Out-of-Home Screen Venue Types

The intention of this document is to standardize a taxonomy of venue types that represent Digital-Out-of-Home (DOOH) advertising screens within a programmatic OpenRTB 2.5 context. The systematization of DOOH venue types will allow for clearer targeting by media buying platforms across a spectrum of available supply-side platforms offering DOOH inventory.

## Versioning & Amendment Process

This specification, written by the contributing parties, is not exhaustive and amenable to changes based on feedback from new participants. However, to facilitate adoption between adopting parties, the frequency of changes shall be maintained on a cadence that respects the level of effort required by currently-integrated parties.

Every attempt will be made to version changes to this specification consistent with [Semantic Versioning](https://semver.org/), with MINOR releases expected on a quarterly cadence. PATCH releases or addressing errata in the specfication will released as needed.

### Version History

| Version | Published         | Notes                                                                                    |
| ------- | ----------------- | ---------------------------------------------------------------------------------------- |
| 1.0.0   | June 4, 2020      | Initial Release                                                                          |
| 1.0.1   | August 4, 2020    | Typos in `bus_shelters`, and misassociation with child siblings in `urban_panels`.       |
| 1.0.2   | October 8, 2020   | Added contributors                                                                       |
| 1.0.3   | October 15, 2020  | Clarification of definition for `entertainment.recreational`                             |
| 1.0.4   | December 18, 2020 | Fixed `station` to `stations` in `transit.train_stations.platform`                       |
| 1.0.5   | February 18, 2021 | Fixed `point of care" definitions                                                        |
| 1.1.0   | March 31, 2021    | New Categories. Compatibility Notes. Clarified Single-Category. Deprecated String values |
| 1.2.0   | March 31, 2023    | New Categories. Compatibility Notes. Removed String values                               |

### Reporting Issues

Issues, Feature Requests, and Bug Reports should be filed as Github Issues in [this project](https://github.com/openooh/venue-taxonomy/issues) and will be reviewed regularly by spec committee members. Parties interested in participating more actively in the specification development process should reach out in 

## Getting Started

Digital Out-of-Home screens, available within a programmatic context, maintain specific geospatial and physical parameters that describe the conditions, environment and/or surroundings. These parameters provide a mutual understanding between buyer and seller within the bidstream and during the transaction phase of trading media.This specification clarifies and classifies these parameters to maintain knowledge equality within the DOOH programmatic industry for all parties involved.

## Definitions & Specification Guidelines

Screen Venue Types should describe an environment and the audience that may be found there. 

A venue type should also describe a media format, except when the media format cannot be separated from the environment. For example, an “ATM” may be in a mall, or a convenience store. The venue type should reflect those parameters.

Screen venue types should not obscure key elements of the environment. 

Venue types should not equate environments that serve dramatically different purposes. For example, it would be insincere to label both Cannabis dispensaries AND pharmacies under the “Wellness” category. These two environments serve very different purposes and audiences, and thus cannot be grouped together.

### Information Tiers

This specification outlines three tiers of precision for programmatic DOOH venue types: Parent Venue Types, Children Venue Types and Grandchildren Venue Types. Each tier is hierarchical and functionally dependent on the higher hierarchy. Moving down the hierarchy chain presents more precise venue information.

### Parent Venue Types

The parent should act as an umbrella grouping for “Child” venue types that share characteristics in common. If the group is logical, a buyer can target the entire grouping and reach similar environments and audiences.

No screens should be solely assigned to a parent venue type, unless that parent venue type has no children.

The parent venue type should provide a high level description of an environment and a general sense of what may occur at the location. For example, the parent venue “Retail” clearly identifies that consumers visit the location to make retail purchases. It does not specify the type of purchase, the specific store names, or the format of the screens in the location.

### Children Venue Types

Children venue types should provide enough detail so that given the parent venue type, a buyer is clear on the environment and what occurs in the location. For example, the child venue type “Retail / Malls” makes it clear that the location is a mall location where retail transactions occur. Since most buyers will share an understanding of what a “mall” is, the child venue type provides the additional clarity needed for a buyer. At the same time, it does not specify the type of mall (indoor vs outdoor, luxury vs budget), or the format of the screens (large spectaculars, TV monitors, kosks).

All venues should be assigned to a child type under a parent venue type, unless the parent venue type has no children.

### Grandchildren Venue Types

Grandchildren venue types provide the most precise contextual geospatial information of the screen. Within certain environments, it is useful to note the functional differences between screen venues. For example, “Transit / Airports / Baggage Claim” is a venue that is functionally different from “Transit / Airports / Gate”. The first venue type traditionally represents passengers leaving the airport, whereas the second venue type may be passengers waiting for a flight departure.

Venues can be assigned to a grandchild but are optional and at the purview of the publisher or supply-side platform to provide. This information may not appear due to lack of the availability of the precise information, or the lack of differentiation needs away from the parent.

## Placement in Bid Requests

In terms of placing venue types, this specification suggests placing venue type information in the device object of an OpenRTB 2.5 `bid_request`. The path would lead into an extension and a subsequent dooh object. The declaration of format is implicit to one the following formats:

* `device.ext.dooh.venuetypelist` (equivalent to `venuetypeid` and any parent-categories of the chosen venue)
* `device.ext.dooh.venuetypeid`
* `device.ext.dooh.venuetypestring` (Deprecated as of 1.1, will be removed in 1.4)

### Implementation Notes:

The values represented in file exports, or `bid_request` should identify the single (best) venue describing the the context and surroundings for where advertising will display. In the event there are multiple classifications in the taxonomy that could apply, media owners should choose the single value most likely to match advertisers expectations.

DSPs receiving bid_reqeusts with unknown categories (e.g. from an SSP sending categories from a more recent version of the specification) should process the `bid_request` as if the category was not present. 
* In the case of a `bid_request` passing only `venuetypeid` this would be equivalent to a request with no defined venue category.
* In the event of a request with `venuetypelist`, if some of the categories in the hierarchy are known, this would be equivalent to a request with just the known parent categories passed (e.g. [`leisure`, `unknown category`] would be interpreted as equivalent to [`leisure`]

## Value Format

The following spec subscribes to UTF-8 encoding.

### Enumeration ID

Each category, regardless of tier, has a unique identifier (ID) that is immutable. DSPs may opt to target this specific ID based on the media they wish to bid on.

### Enumerated List

The enumerated list can be passed in the bid request. It is a comma-separated array of category IDs from the preceding and dependent tiers. Should only a parent-child category be associated with the screen’s venue, the array will be composed of two enumerated IDs. Refer to the summary chart for further details.

## Parent Categories & IDs

| Parent Category  | Enumeration ID |
| ---------------- | -------------- |
| Transit          | 1              |
| Retail           | 2              |
| Outdoor          | 3              |
| Health & Beauty  | 4              |
| Point of Care    | 5              |
| Education        | 6              |
| Office Buildings | 7              |
| Leisure          | 8              |
| Government       | 9              |
| Financial        | 10             |
| Residential      | 11             |

## Child Categories & IDs

### Transit

| Child Category       | Category Definition                            | Enumeration ID |
| -------------------- | ---------------------------------------------- | -------------- |
| Airports             | Signage located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges.                                           | 101 |
| Buses                | Displays located on or in city or intercity buses.                 | 102 |
| Taxi & Rideshare TV  | Advertising displays placed inside taxis and rideshare vehicles visible to passengers in the back seat. | 103 |
| Taxi & Rideshare Top | Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers. | 104 |
| Subway               | Advertising displays placed inside subway trains or inside stations or on subway platforms. | 105 |
| Train Stations       | Advertising displays placed inside train stations or on platforms. | 106 |
| Ferry                | Advertising displays placed inside a passenger water transport.    | 107 |

### Retail

| Child Category        | Category Definition                             | Enumeration ID |
| --------------------- | ----------------------------------------------- | -------------- | 
| Fueling Stations      | An establishment beside a road selling fuel for motor vehicles. | 201 |
| Convenience Stores    | A store with extended opening hours and in a convenient location, stocking a limited range of household goods and groceries. | 202 |
| Grocery               | A retail shop that primarily sells food, either fresh or preserved. | 203 |
| Liquor Stores         | A retail shop that predominantly sells prepackaged alcoholic beverages, typically in bottles, intended to be consumed off the store’s premises. | 204 |
| Mall                  | A large building or series of connected buildings containing a variety of retail stores and typically also restaurants. | 205 |
| Cannabis Dispensaries | A store that sells and dispenses cannabis and CBD products. | 206 |
| Pharmacies            | A store where medicinal drugs are dispensed and sold. | 207 |
| Parking Garages       | A building in which people usually pay to park their cars, trucks and other vehicles. | 208 |

### Outdoor

| Child Category | Category Definition                             | Enumeration ID |
| -------------- | ----------------------------------------------- | -------------- | 
| Billboards     | Located primarily on major roads, they attract high-density consumer exposure (mostly to vehicular traffic, but often to pedestrians). | 301 |
| Urban Panels   | Digital screens in urban environments, typically providing a public amenity. Typically visible to pedestrians and in some cases, vehicular traffic as well. | 302 |
| Bus Shelters   | Enclosures where individuals may wait for buses in an urban environment. Signage may be attached to the interior or exterior of the enclosure.       | 303 |


### Health & Beauty

| Child Category | Category Definition                         | Enumeration ID |
| -------------- | ------------------------------------------- | -------------- |
| Gyms           | A club, building, or large room, usually containing special equipment, where people go to do physical exercise and get fit. | 401 |
| Salons         | An establishment where a hairdresser, beautician, or couturier conducts business. | 402 |
| Spas           | A commercial establishment offering health and beauty treatment through such means as steam baths, exercise equipment, and massage. | 403 |

### Point of Care

| Child Category     | Category Definition                         | Enumeration ID |
| ------------------ | ------------------------------------------- | -------------- |
| Doctor’s Offices   | Non-hospital facility run by a physician - for treatment of people. | 501 |
| Veterinary Offices | Non-hopsital facility run by a veterinarian - for treatment of animals. | 502 |

### Education

| Child Category            | Category Definition                            | Enumeration ID |
| ------------------------- | ---------------------------------------------- | -------------- |
| Schools                   | An educational institution designed to provide learning spaces and learning environments for the teaching of students between K - 12 under the direction of teachers. | 601 |
| Colleges and Universities | An education institution designed for instruction, examination, or both, of students  in many branches of advanced learning, conferring degrees in various faculties, and often embodying colleges and similar institutions. | 602 |

### Office Buildings

| Child Category   | Category Definition                         | Enumeration ID | 
| ---------------- | ------------------------------------------- | -------------- | 
| Office Buildings | An office building, also known as an office block or business center is a form of commercial building which contains spaces mainly designed to be used for offices. Advertising displays may be in building lobbies, common areas, or in elevators.     | 701 |

### Leisure

| Child Category         | Category Definition                            | Enumeration ID |
| ---------------------- | ---------------------------------------------- | -------------- |
| Recreational Locations | Location where recreational and/or leisure activities take place. | 801 |
| Movie Theaters         | Location for displaying long-format content on large screens. | 802 |
| Sports Entertainment   | A venue that individuals or groups can play an active sport or activity.| 803 |
| Bars                   | A retail business that serves alcoholic beverages. | 804 |
| Casual Dining          | A restaurant that serves moderately priced food in a casual atmosphere. | 805 |
| QSR                    | A fast food restaurant, also known as a quick service restaurant within the industry, is a specific type of restaurant that serves fast-food cuisine and has minimal table service. | 806            |
| Hotels                 | An establishment providing accommodations, means, and other services for travelers and tourists.                     | 807            |
| Golf Carts             | A small motorized vehicle for golfers and their equipment.      | 808            |
| Night Clubs            | An establishment for nighttime entertainment, typically serving drinks and offering music, dancing, etc.   | 809            |
| High-End Dining        |  A restaurant that serves expensive food. Often in a more formal atmosphere, and accepting or requiring reservations | 810            |

### Government

| Child Category | Category Definition                                                                                        | Enumeration ID |
| -------------- | ---------------------------------------------------------------------------------------------------------- | -------------- |
| DMVs           | An office building, also known as an office block or business center is a form of commercial building which contains spaces mainly designed to be used for offices. Advertising displays may be in building lobbies, common areas, or in elevators.                          | 901            |
| Military Bases | A facility that houses and facilitates training for military personnel and operations.                     | 902            |
| Post Offices   | A facility that handles the receipt, delivery, and processing of mail, packages, or other postal services. | 903            |

### Financial

| Child Category | Category Definition                                                                | Enumeration Value |
| -------------- | ---------------------------------------------------------------------------------- | ----------------- |
| Banks          | A bank is a financial institution licensed to store or invest accountholders money | 1001              |

### Residential

| Child Category                       | Category Definition                                  | Enumeration Value |
| ------------------------------------ | ---------------------------------------------------- | ----------------- |
| Apartment Buildings and Condominiums | A building that contains different residential units | 1101              |

## Grandchild Categories & IDs

### Transit: Airports

| Grandchild Category | Category Definition                                                           | Enumeration ID |
| ------------------- | ----------------------------------------------------------------------------- | -------------- |
| Arrival Hall        | Locations for meeting passengers arriving on flights                          | 10101          |
| Baggage Claim       | Locations to retrieve baggage not carried during a flight                     | 10102          |
| Departures Hall     | Location for dropping off passengers leaving on flights                       | 10103          |
| Food Court          | Location within an airport for food, typically casual                         | 10104          |
| Gates               | Location to wait for or embark or disembark from a specific plane             | 10105          |
| Lounges             | (typically private) places to wait for flights, separate from public spaces   | 10106          |
| Shopping Area       | Retail areas contained within facilities primarily used for servicing flights | 10107          |

### Transit: Buses

| Grandchild Category | Category Definition                                                       | Enumeration ID |
| ------------------- | ------------------------------------------------------------------------- | -------------- |
| Bus (Inside)        | Advertising inside a bus, primarily visible to bus passengers             | 10201          |
| Terminal            | Advertising at facilities for embarking or disembarking from a bus        | 10202          |
| Bus (Outside)       | Advertising outside a bus, primarily visible to people not riding the bus | 10203          |

### Transit: Subway

| Grandchild Category | Category Definition                                                 | Enumeration ID |
| ------------------- | ------------------------------------------------------------------- | -------------- |
| Subway Train        | A (typical municipal area) train that travels primarily underground | 10501          |
| Platform            | Areas to wait for, board, or unboard a subway                       | 10502          |

### Transit: Train Stations

| Grandchild Category | Category Definition                                          | Enumeration ID |
| ------------------- | ------------------------------------------------------------ | -------------- |
| Train               | A train that travels primarily above ground, on rails\       | 10601          |
| Platform            | Areas to wait for, board, or unboard a train                 | 10602          |

### Retail: Fueling Stations

| Grandchild Category | Category Definition                                                              | Enumeration ID |
| ------------------- | -------------------------------------------------------------------------------- | -------------- |
| Fuel Dispenser      | A (typically self-service) device for dispensing fuel to vehicles.               | 20101          |
| Shop                | A store attached to a location who's primary audience is people fueling vehicles | 20102          |

### Retail: Grocery

| Grandchild Category | Category Definition                                                             | Enumeration ID |
| ------------------- | ------------------------------------------------------------------------------- | -------------- |
| Shop Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 20301          |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 20302          |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 20303          |

### Retail: Malls

| Grandchild Category | Category Definition                                                                          | Enumeration ID |
| ------------------- | -------------------------------------------------------------------------------------------- | -------------- |
| Concourse           | A large open area (including hallways and escalators)                                        | 20501          |
| Food Court          | A Common area with multiple food vendors and common tables.                                  | 20502          |
| Spectacular         | Large and impactful screen(s) at a prime location. It often utilizes special embellishments. | 20503          |

### Outdoor: Billboards

| Grandchild Category | Category Definition                                                                                         | Enumeration ID |
| ------------------- | ----------------------------------------------------------------------------------------------------------- | -------------- |
| Roadside            | Primarily vehicular environments                                                                            | 30101          |
| Highway             | High-speed vehicular environments, typically with controlled entrance/exit (e.g. "exits" or "interchanges") | 30102          |
| Spectacular         | A bulletin that is usually larger than 14’ x 48’ and is positioned at a prime location in a market. A spectacular often utilizes special embellishments.       | 30103          |

### Health and Beauty: Gyms

| Grandchild Category | Category Definition                                                           | Enumeration ID |
| ------------------- | ----------------------------------------------------------------------------- | -------------- |
| Lobby               | Area for waiting or meeting guests                                            | 40101          |
| Fitness Equipment   | Area primarily for exercise or the usage of fitness equipment                 | 40102          |

### Health and Beauty: Salons

| Grandchild Category  | Category Definition                      | Enumeration ID |
| -------------------- | ---------------------------------------- | -------------- |
| Unisex Salon         | Salon catering to clients of any sex     | 40201          |
| Men's Salon          | Salon primarily catering towards men     | 40202          |
| Women's Salon        | Salon primarily catering towards women   | 40203          |

### Education: Colleges and Universities

| Grandchild Category   | Category Definition                                    | Enumeration ID |
| --------------------- | ------------------------------------------------------ | -------------- |
| Residences            | Places where faculty or students live                  | 60201          |
| Common Areas          | Shared spaces for study, dining, or leisure activities | 60202          |
| Athletic Facilities   | Facillities or stadiums for sporting competition       | 60203          |

### Office Buildings: Office Buildings

| Grandchild Category | Category Definition                                                                                      | Enumeration ID |
| ------------------- | -------------------------------------------------------------------------------------------------------- | -------------- |
| Elevator            | Enclosed, Vertical conveyance for people and goods                                                       | 70101          |
| Lobby               | Common space for tenants to meet and greet visitors and guests, typically near entrances                 | 70102          |

### Leisure: Recreational Locations

| Grandchild Category   | Category Definition                                              | Enumeration ID |
| --------------------- | ---------------------------------------------------------------- | -------------- |
| Theme Parks           | An amusement park with a unifying setting or idea.               | 80101          |
| Museums and Galleries | A building in which objects of historical, scientific, artistic, or cultural interest are stored and exhibited. e.g. "the Museum of Modern Art"                 | 80102          |
| Concert Venues        | Any location used for a concert or musical performance           | 80103          |

### Leisure: Movie Theaters

| Grandchild Category | Category Definition | Enumeration ID |
| ------------------- | ------------------- | -------------- |
| Lobby               | A corridor or hall connected with a larger room or series of rooms and used as a passageway or waiting room: such as a large hall serving as a foyer (as of a hotel or theater)                 | 80201          |
| Food Court          | An area within a building (such as a shopping mall) set apart for food concessions.                 | 80202          |

### Leisure: Sports Entertainment

| Grandchild Category | Category Definition | Enumeration ID |
| ------------------- | ------------------- | -------------- |
| Sport Arena         | A central area used for sports or other forms of entertainment and surrounded by seats for spectators. | 80301          |
| Club House          | Locker rooms used by an athletic team                 | 80302          |

### Leisure: Hotels

| Grandchild Category | Category Definition                                                     | Enumeration ID |
| ------------------- | ----------------------------------------------------------------------- | -------------- |
| Lobby               | Commonly accessible shared spaces for guests at a hotel                 | 80701          |
| Elevator            | Commonly accessible, enclosed spaces used to move between floors.       | 80702          |
| Room                | Locations occupied and restricted to a single guest                     | 80703          |

### Residential: Apartment Buildings and Condominiums

| Grandchild Category | Category Definition | Enumeration ID |
| ------------------- | ------------------- | -------------- |
| Lobby               | A corridor or hall connected with a larger room or series of rooms and used as a passageway or waiting room: such as a large hall serving as a foyer (as of a hotel or theater)                 | 110101         |
| Elevator            | Enclosed, Vertical conveyance for people and goods                   | 110102         |
