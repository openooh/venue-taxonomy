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

### String Values (Deprecated - Targeted for Removal in 1.4 / 2021Q4)

String values are text-based identifiers of venue categories. Dependencies on parent and child tiers use a period connector for tier separation. All unique text identifiers are lower case, and combination words utilize the standard underscore. String values may be used as substitutions for enumeration values and enumerated lists and provide greater flexibility for implementation.

In order to ease forwards-compatibility, internationalization, and consistency as the names and definitions of categories evolve, string descriptions as a wire protocol are deprecated as of 1.1, and will be removed in 1.4 (targeted for approximately 2021Q4). Implementors should use Enumeration IDs for persistance or wire-level transmission.

## Parent Categories & IDs
|Parent Category|Enumeration ID|String Value|
|---|---|---|
|Transit|1|transit|
|Retail|2|retail|
|Outdoor|3|outdoor|
|Health &amp; Beauty|4|health_beauty|
|Point of Care|5|point_care|
|Education|6|education|
|Office Buildings|7|office_buildings|
|Leisure|8|entertainment|
|Government|9|government|
|Financial|10|financial|
|Residential|11|residential|

## Child Categories & IDs
### Transit
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Airports|Signage located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges.|101|transit.airports|
|Buses|Displays located on or in city or intercity buses.|102|transit.buses|
|Taxi & Rideshare TV|Advertising displays placed inside taxis and rideshare vehicles visible to passengers in the back seat.|103|transit.taxi_rideshare_tv|
|Taxi & Rideshare Top|Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers.|104|transit.taxi_rideshare_top|
|Subway|Advertising displays placed inside subway trains or inside stations or on subway platforms.|105|transit.subway|
|Train Stations|Advertising displays placed inside train stations or on platforms.|106|transit.train_stations|
|Ferry|Advertising displays placed inside a passenger water transport.|107|transit.ferry|

### Retail
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Fueling Stations|An establishment beside a road selling fuel for motor vehicles.|201|retail.gas_stations|
|Convenience Stores|A store with extended opening hours and in a convenient location, stocking a limited range of household goods and groceries.|202|retail.convenience_store|
|Grocery|A retail shop that primarily sells food, either fresh or preserved.|203|retail.grocery|
|Liquor Stores|A retail shop that predominantly sells prepackaged alcoholic beverages, typically in bottles, intended to be consumed off the store’s premises.|204|retail.liquor_stores|
|Mall|A large building or series of connected buildings containing a variety of retail stores and typically also restaurants.|205|retail.malls|
|Cannabis Dispensaries|A store that sells and dispenses cannabis and CBD products.|206|retail.dispensaries|
|Pharmacies|A store where medicinal drugs are dispensed and sold.|207|retail.pharmacies|
|Parking Garages|A building in which people usually pay to park their cars, trucks and other vehicles.|208|retail.parking_garages|

### Outdoor
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Billboards|Located primarily on major roads, they attract high-density consumer exposure (mostly to vehicular traffic, but often to pedestrians).|301|outdoor.billboards|
|Urban Panels|Digital screens in urban environments, typically providing a public amenity. Typically visible to pedestrians and in some cases, vehicular traffic as well.|302|outdoor.urban_panels|
|Bus Shelters|Enclosures where individuals may wait for buses in an urban environment. Signage may be attached to the interior or exterior of the enclosure.|303|outdoor.bus_shelters|

### Health &amp; Beauty
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Gyms|A club, building, or large room, usually containing special equipment, where people go to do physical exercise and get fit.|401|health_beauty.gyms|
|Salons|An establishment where a hairdresser, beautician, or couturier conducts business.|402|health_beauty.salons|
|Spas|A commercial establishment offering health and beauty treatment through such means as steam baths, exercise equipment, and massage.|403|health_beauty.spas|

### Point of Care
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Doctor’s Offices|Non-hospital facility run by a physician - for treatment of people.|501|point_care.doctor_offices|
|Veterinary Offices|Non-hopsital facility run by a veterinarian - for treatment of animals.|502|point_care.veterinary_offices|

### Education
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Schools|An educational institution designed to provide learning spaces and learning environments for the teaching of students between K - 12 under the direction of teachers.|601|education.schools|
|Colleges and Universities|An education institution designed for instruction, examination, or both, of students in many branches of advanced learning, conferring degrees in various faculties, and often embodying colleges and similar institutions.|602|education.colleges|

### Office Buildings
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Office Buildings|An office building, also known as an office block or business center is a form of commercial building which contains spaces mainly designed to be used for offices. Advertising displays may be in building lobbies, common areas, or in elevators.|701|office_buildings.office_buildings|

### Leisure
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Recreational Locations|Location where recreational and/or leisure activities take place.|801|entertainment.recreational|
|Movie Theaters|Location for displaying long-format content on large screens.|802|entertainment.movie_theaters|
|Sports Entertainment|A venue that individuals or groups can play an active sport or activity.|803|entertainment.sports|
|Bars|A retail business that serves alcoholic beverages.|804|entertainment.bars|
|Casual Dining|A restaurant that serves moderately priced food in a casual atmosphere.|805|entertainment.casual_dining|
|QSR|A fast food restaurant, also known as a quick service restaurant within the industry, is a specific type of restaurant that serves fast-food cuisine and has minimal table service.|806|entertainment.qsr|
|Hotels|An establishment providing accommodations, means, and other services for travelers and tourists.|807|entertainment.hotels|
|Golf Carts|A small motorized vehicle for golfers and their equipment.|808|entertainment.golf_cart|
|Night Clubs|An establishment for nighttime entertainment, typically serving drinks and offering music, dancing, etc.|809|entertainment.night_club|
|High-End Dining|A restaurant that serves expensive food. Often in a more formal atmosphere, and accepting or requiring reservations|810|entertainment.high_end_dining|

### Government
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|DMVs|An office building, also known as an office block or business center is a form of commercial building which contains spaces mainly designed to be used for offices. Advertising displays may be in building lobbies, common areas, or in elevators.|901|government.dmv|
|Military Bases|A facility that houses and facilitates training for military personnel and operations.|902|government.military_bases|
|Post Offices|A facility that handles the receipt, delivery, and processing of mail, packages, or other postal services.|903|government.postal|

### Financial
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Banks|A bank is a financial institution licensed to store or invest accountholders money|1001|financial.banks|

### Residential
|Child Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Apartment Buildings and Condominiums|A building that contains different residential units|1101|residential.apartment|

## Grandchild Categories & IDs
### Transit : Airports
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Airports|Signage located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges.|101|transit.airports|
|Buses|Displays located on or in city or intercity buses.|102|transit.buses|
|Taxi & Rideshare TV|Advertising displays placed inside taxis and rideshare vehicles visible to passengers in the back seat.|103|transit.taxi_rideshare_tv|
|Taxi & Rideshare Top|Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers.|104|transit.taxi_rideshare_top|
|Subway|Advertising displays placed inside subway trains or inside stations or on subway platforms.|105|transit.subway|
|Train Stations|Advertising displays placed inside train stations or on platforms.|106|transit.train_stations|
|Ferry|Advertising displays placed inside a passenger water transport.|107|transit.ferry|

### Transit : Buses
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Airports|Signage located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges.|101|transit.airports|
|Buses|Displays located on or in city or intercity buses.|102|transit.buses|
|Taxi & Rideshare TV|Advertising displays placed inside taxis and rideshare vehicles visible to passengers in the back seat.|103|transit.taxi_rideshare_tv|
|Taxi & Rideshare Top|Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers.|104|transit.taxi_rideshare_top|
|Subway|Advertising displays placed inside subway trains or inside stations or on subway platforms.|105|transit.subway|
|Train Stations|Advertising displays placed inside train stations or on platforms.|106|transit.train_stations|
|Ferry|Advertising displays placed inside a passenger water transport.|107|transit.ferry|

### Transit : Subway
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Airports|Signage located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges.|101|transit.airports|
|Buses|Displays located on or in city or intercity buses.|102|transit.buses|
|Taxi & Rideshare TV|Advertising displays placed inside taxis and rideshare vehicles visible to passengers in the back seat.|103|transit.taxi_rideshare_tv|
|Taxi & Rideshare Top|Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers.|104|transit.taxi_rideshare_top|
|Subway|Advertising displays placed inside subway trains or inside stations or on subway platforms.|105|transit.subway|
|Train Stations|Advertising displays placed inside train stations or on platforms.|106|transit.train_stations|
|Ferry|Advertising displays placed inside a passenger water transport.|107|transit.ferry|

### Transit : Train Stations
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Airports|Signage located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges.|101|transit.airports|
|Buses|Displays located on or in city or intercity buses.|102|transit.buses|
|Taxi & Rideshare TV|Advertising displays placed inside taxis and rideshare vehicles visible to passengers in the back seat.|103|transit.taxi_rideshare_tv|
|Taxi & Rideshare Top|Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers.|104|transit.taxi_rideshare_top|
|Subway|Advertising displays placed inside subway trains or inside stations or on subway platforms.|105|transit.subway|
|Train Stations|Advertising displays placed inside train stations or on platforms.|106|transit.train_stations|
|Ferry|Advertising displays placed inside a passenger water transport.|107|transit.ferry|

### Retail : Fueling Stations
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Fueling Stations|An establishment beside a road selling fuel for motor vehicles.|201|retail.gas_stations|
|Convenience Stores|A store with extended opening hours and in a convenient location, stocking a limited range of household goods and groceries.|202|retail.convenience_store|
|Grocery|A retail shop that primarily sells food, either fresh or preserved.|203|retail.grocery|
|Liquor Stores|A retail shop that predominantly sells prepackaged alcoholic beverages, typically in bottles, intended to be consumed off the store’s premises.|204|retail.liquor_stores|
|Mall|A large building or series of connected buildings containing a variety of retail stores and typically also restaurants.|205|retail.malls|
|Cannabis Dispensaries|A store that sells and dispenses cannabis and CBD products.|206|retail.dispensaries|
|Pharmacies|A store where medicinal drugs are dispensed and sold.|207|retail.pharmacies|
|Parking Garages|A building in which people usually pay to park their cars, trucks and other vehicles.|208|retail.parking_garages|

### Retail : Grocery
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Fueling Stations|An establishment beside a road selling fuel for motor vehicles.|201|retail.gas_stations|
|Convenience Stores|A store with extended opening hours and in a convenient location, stocking a limited range of household goods and groceries.|202|retail.convenience_store|
|Grocery|A retail shop that primarily sells food, either fresh or preserved.|203|retail.grocery|
|Liquor Stores|A retail shop that predominantly sells prepackaged alcoholic beverages, typically in bottles, intended to be consumed off the store’s premises.|204|retail.liquor_stores|
|Mall|A large building or series of connected buildings containing a variety of retail stores and typically also restaurants.|205|retail.malls|
|Cannabis Dispensaries|A store that sells and dispenses cannabis and CBD products.|206|retail.dispensaries|
|Pharmacies|A store where medicinal drugs are dispensed and sold.|207|retail.pharmacies|
|Parking Garages|A building in which people usually pay to park their cars, trucks and other vehicles.|208|retail.parking_garages|

### Retail : Mall
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Fueling Stations|An establishment beside a road selling fuel for motor vehicles.|201|retail.gas_stations|
|Convenience Stores|A store with extended opening hours and in a convenient location, stocking a limited range of household goods and groceries.|202|retail.convenience_store|
|Grocery|A retail shop that primarily sells food, either fresh or preserved.|203|retail.grocery|
|Liquor Stores|A retail shop that predominantly sells prepackaged alcoholic beverages, typically in bottles, intended to be consumed off the store’s premises.|204|retail.liquor_stores|
|Mall|A large building or series of connected buildings containing a variety of retail stores and typically also restaurants.|205|retail.malls|
|Cannabis Dispensaries|A store that sells and dispenses cannabis and CBD products.|206|retail.dispensaries|
|Pharmacies|A store where medicinal drugs are dispensed and sold.|207|retail.pharmacies|
|Parking Garages|A building in which people usually pay to park their cars, trucks and other vehicles.|208|retail.parking_garages|

### Outdoor : Billboards
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Billboards|Located primarily on major roads, they attract high-density consumer exposure (mostly to vehicular traffic, but often to pedestrians).|301|outdoor.billboards|
|Urban Panels|Digital screens in urban environments, typically providing a public amenity. Typically visible to pedestrians and in some cases, vehicular traffic as well.|302|outdoor.urban_panels|
|Bus Shelters|Enclosures where individuals may wait for buses in an urban environment. Signage may be attached to the interior or exterior of the enclosure.|303|outdoor.bus_shelters|

### Health &amp; Beauty : Gyms
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Gyms|A club, building, or large room, usually containing special equipment, where people go to do physical exercise and get fit.|401|health_beauty.gyms|
|Salons|An establishment where a hairdresser, beautician, or couturier conducts business.|402|health_beauty.salons|
|Spas|A commercial establishment offering health and beauty treatment through such means as steam baths, exercise equipment, and massage.|403|health_beauty.spas|

### Health &amp; Beauty : Salons
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Gyms|A club, building, or large room, usually containing special equipment, where people go to do physical exercise and get fit.|401|health_beauty.gyms|
|Salons|An establishment where a hairdresser, beautician, or couturier conducts business.|402|health_beauty.salons|
|Spas|A commercial establishment offering health and beauty treatment through such means as steam baths, exercise equipment, and massage.|403|health_beauty.spas|

### Education : Colleges and Universities
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Schools|An educational institution designed to provide learning spaces and learning environments for the teaching of students between K - 12 under the direction of teachers.|601|education.schools|
|Colleges and Universities|An education institution designed for instruction, examination, or both, of students in many branches of advanced learning, conferring degrees in various faculties, and often embodying colleges and similar institutions.|602|education.colleges|

### Office Buildings : Office Buildings
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Office Buildings|An office building, also known as an office block or business center is a form of commercial building which contains spaces mainly designed to be used for offices. Advertising displays may be in building lobbies, common areas, or in elevators.|701|office_buildings.office_buildings|

### Leisure : Recreational Locations
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Recreational Locations|Location where recreational and/or leisure activities take place.|801|entertainment.recreational|
|Movie Theaters|Location for displaying long-format content on large screens.|802|entertainment.movie_theaters|
|Sports Entertainment|A venue that individuals or groups can play an active sport or activity.|803|entertainment.sports|
|Bars|A retail business that serves alcoholic beverages.|804|entertainment.bars|
|Casual Dining|A restaurant that serves moderately priced food in a casual atmosphere.|805|entertainment.casual_dining|
|QSR|A fast food restaurant, also known as a quick service restaurant within the industry, is a specific type of restaurant that serves fast-food cuisine and has minimal table service.|806|entertainment.qsr|
|Hotels|An establishment providing accommodations, means, and other services for travelers and tourists.|807|entertainment.hotels|
|Golf Carts|A small motorized vehicle for golfers and their equipment.|808|entertainment.golf_cart|
|Night Clubs|An establishment for nighttime entertainment, typically serving drinks and offering music, dancing, etc.|809|entertainment.night_club|
|High-End Dining|A restaurant that serves expensive food. Often in a more formal atmosphere, and accepting or requiring reservations|810|entertainment.high_end_dining|

### Leisure : Movie Theaters
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Recreational Locations|Location where recreational and/or leisure activities take place.|801|entertainment.recreational|
|Movie Theaters|Location for displaying long-format content on large screens.|802|entertainment.movie_theaters|
|Sports Entertainment|A venue that individuals or groups can play an active sport or activity.|803|entertainment.sports|
|Bars|A retail business that serves alcoholic beverages.|804|entertainment.bars|
|Casual Dining|A restaurant that serves moderately priced food in a casual atmosphere.|805|entertainment.casual_dining|
|QSR|A fast food restaurant, also known as a quick service restaurant within the industry, is a specific type of restaurant that serves fast-food cuisine and has minimal table service.|806|entertainment.qsr|
|Hotels|An establishment providing accommodations, means, and other services for travelers and tourists.|807|entertainment.hotels|
|Golf Carts|A small motorized vehicle for golfers and their equipment.|808|entertainment.golf_cart|
|Night Clubs|An establishment for nighttime entertainment, typically serving drinks and offering music, dancing, etc.|809|entertainment.night_club|
|High-End Dining|A restaurant that serves expensive food. Often in a more formal atmosphere, and accepting or requiring reservations|810|entertainment.high_end_dining|

### Leisure : Sports Entertainment
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Recreational Locations|Location where recreational and/or leisure activities take place.|801|entertainment.recreational|
|Movie Theaters|Location for displaying long-format content on large screens.|802|entertainment.movie_theaters|
|Sports Entertainment|A venue that individuals or groups can play an active sport or activity.|803|entertainment.sports|
|Bars|A retail business that serves alcoholic beverages.|804|entertainment.bars|
|Casual Dining|A restaurant that serves moderately priced food in a casual atmosphere.|805|entertainment.casual_dining|
|QSR|A fast food restaurant, also known as a quick service restaurant within the industry, is a specific type of restaurant that serves fast-food cuisine and has minimal table service.|806|entertainment.qsr|
|Hotels|An establishment providing accommodations, means, and other services for travelers and tourists.|807|entertainment.hotels|
|Golf Carts|A small motorized vehicle for golfers and their equipment.|808|entertainment.golf_cart|
|Night Clubs|An establishment for nighttime entertainment, typically serving drinks and offering music, dancing, etc.|809|entertainment.night_club|
|High-End Dining|A restaurant that serves expensive food. Often in a more formal atmosphere, and accepting or requiring reservations|810|entertainment.high_end_dining|

### Leisure : Hotels
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Recreational Locations|Location where recreational and/or leisure activities take place.|801|entertainment.recreational|
|Movie Theaters|Location for displaying long-format content on large screens.|802|entertainment.movie_theaters|
|Sports Entertainment|A venue that individuals or groups can play an active sport or activity.|803|entertainment.sports|
|Bars|A retail business that serves alcoholic beverages.|804|entertainment.bars|
|Casual Dining|A restaurant that serves moderately priced food in a casual atmosphere.|805|entertainment.casual_dining|
|QSR|A fast food restaurant, also known as a quick service restaurant within the industry, is a specific type of restaurant that serves fast-food cuisine and has minimal table service.|806|entertainment.qsr|
|Hotels|An establishment providing accommodations, means, and other services for travelers and tourists.|807|entertainment.hotels|
|Golf Carts|A small motorized vehicle for golfers and their equipment.|808|entertainment.golf_cart|
|Night Clubs|An establishment for nighttime entertainment, typically serving drinks and offering music, dancing, etc.|809|entertainment.night_club|
|High-End Dining|A restaurant that serves expensive food. Often in a more formal atmosphere, and accepting or requiring reservations|810|entertainment.high_end_dining|

### Residential : Apartment Buildings and Condominiums
|Grandchild Category|Category Definition|Enumeration ID|String Value|
|---|---|---|---|
|Apartment Buildings and Condominiums|A building that contains different residential units|1101|residential.apartment|


