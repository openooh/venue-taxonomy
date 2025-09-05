# Digital Out-of-Home Screen Venue Types

The intention of this document is to standardize a taxonomy of venue types that represent Digital-Out-of-Home (DOOH) advertising screens within a programmatic OpenRTB 2.6 context. The systematization of DOOH venue types will allow for clearer targeting by media buying platforms across a spectrum of available supply-side platforms offering DOOH inventory.

## Versioning & Amendment Process

This specification, written by the contributing parties, is not exhaustive and amenable to changes based on feedback from new participants. However, to facilitate adoption between adopting parties, the frequency of changes shall be maintained on a cadence that respects the level of effort required by currently-integrated parties.

Every attempt will be made to version changes to this specification consistent with [Semantic Versioning](https://semver.org/), with MINOR releases expected on a bi-annual cadence. PATCH releases or addressing errata in the specfication will released as needed.

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
| 1.2.0   | September 3, 2025 | New Categories. Ammended Categories. Deprecated Categories. Updated list of contributors. Updated language for 2.6 spec request requirements |

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

Children venue types should provide enough detail so that given the parent venue type, a buyer is clear on the environment and what occurs in the location. For example, the child venue type “Retail / Malls” makes it clear that the location is a mall location where retail transactions occur. Since most buyers will share an understanding of what a “mall” is, the child venue type provides the additional clarity needed for a buyer. At the same time, it does not specify the type of mall (indoor vs outdoor, luxury vs budget), or the format of the screens (large spectaculars, TV monitors, kiosks).

All venues should be assigned to a child type under a parent venue type, unless the parent venue type has no children.

### Grandchildren Venue Types

Grandchildren venue types provide the most precise contextual geospatial information of the screen. Within certain environments, it is useful to note the functional differences between screen venues. For example, “Transit / Airports / Baggage Claim” is a venue that is functionally different from “Transit / Airports / Gate”. The first venue type traditionally represents passengers leaving the airport, whereas the second venue type may be passengers waiting for a flight departure.

Venues can be assigned to a grandchild but are optional and at the purview of the publisher or supply-side platform to provide. This information may not appear due to lack of the availability of the precise information, or the lack of differentiation needs away from the parent.

## Placement in Bid Requests

In terms of placing venue types, this specification suggests placing venue type information in the device object of an OpenRTB 2.6 `bid_request`. The path would lead into an extension and a subsequent dooh object. The declaration of format is implicit to one the following formats:

* `device.ext.dooh.venuetypelist` (equivalent to `venuetypeid` and any parent-categories of the chosen venue)
* `device.ext.dooh.venuetypeid`

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

### String Values (Deprecated)



## Parent Categories & IDs

| Parent Category  | Enumeration ID | String Value (Deprecated) |
| ---------------- | -------------- | ------------------------- |
| Transit          | 1              | transit                   |
| Retail           | 2              | retail                    |
| Outdoor          | 3              | outdoor                   |
| Health & Beauty  | 4              | health_beauty             |
| Point of Care    | 5              | point_care                |
| Education        | 6              | education                 |
| Office Buildings | 7              | office_buildings          |
| Leisure          | 8              | entertainment             |
| Government       | 9              | government                |
| Financial        | 10             | financial                 |
| Residential      | 11             | residential               |

## Child Categories & IDs

### Transit

| Child Category       | Category Definition                            | Enumeration ID | String Value (Deprecated)  |
| -------------------- | ---------------------------------------------- | -------------- | -------------------------- |
| Airports             | Signage located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges.                                                                     | 101 | transit.airports |
| Buses                | Displays located on or in city or intercity buses.                 | 102 | transit.buses |
| Taxi & Rideshare TV  | Advertising displays placed inside taxis and rideshare vehicles visible to passengers in the back seat. | 103 | transit.taxi\_rideshare\_tv |
| Taxi & Rideshare Top | (DEPRECATED) - See Outdoor Category (ID - 307) Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers. | 104 | transit.taxi\_rideshare\_top |
| Subway               | Advertising displays placed inside subway trains or inside stations or on subway platforms. | 105 | transit.subway |
| Train Stations       | Advertising displays placed inside train stations or on platforms. | 106 | transit.train\_stations    |
| Ferry                | Advertising displays placed inside a passenger water transport.    | 107 | transit.ferry     |
| Tram                 | Displays placed on the interior, exterior, or at the stations of urban light rail trams or streetcars.    | 108 | transit.tram     |
| Ferry                | A rest area or service stop designed for drivers, often found along highways or motorways. These areas provide facilities like fuel stations, restaurants and restrooms.    | 109 | transit.highway\_rest\_area     |

### Retail

| Child Category        | Category Definition                             | Enumeration ID | String Value (Deprecated)|
| --------------------- | ----------------------------------------------- | -------------- | ------------------------ |
| Fueling Stations      | An establishment beside a road selling fuel for motor vehicles. | 201 | retail.gas\_stations |
| Convenience Stores    | A store with extended opening hours and in a convenient location, stocking a limited range of household goods and groceries. | 202 | retail.convenience\_store |
| Grocery               | A retail shop that primarily sells food, either fresh or preserved. | 203 | retail.grocery |
| Liquor Stores         | A retail shop that predominantly sells prepackaged alcoholic beverages, typically in bottles, intended to be consumed off the store’s premises. | 204 | retail.liquor\_stores |
| Mall                  | A large building or series of connected buildings containing a variety of retail stores and typically also restaurants. | 205 | retail.malls |
| Cannabis Dispensaries | A store that sells and dispenses cannabis and CBD products. | 206 | retail.dispensaries |
| Pharmacies            | A store where medicinal drugs are dispensed and sold. | 207 | retail.pharmacies |
| Parking Garages       | A building in which people usually pay to park their cars, trucks and other vehicles. | 208 | retail.parking\_garages |
| Furniture             | An establishment that sells furniture. | 209 | retail.furniture |
| Apparel               | An establishment that sells clothing and accessories. | 210 | retail.apparel |
| Automotive            | An establishment where a person engages in the Business of selling, offering for sale, or providing servicing or maintenance of a motor vehicle. | 211 | retail.automotive |
| Laundromat            | An establishment with coin-operated washing machines and dryers for public use. | 212 | retail.laundromat |
| Vape Shop             | An establishment specializing in the selling of vaping products. | 213 | retail.vape\_shop |
| Mass Merchandising    | An establishment with a wide range of goods where customers can purchase products, sometimes in bulk. | 214 | retail.mass\_merchandising |
| Consumer Electronics  | An establishment that sells electronic devices intended for personal or household use, such as appliances, home entertainment systems, and communication devices. These stores may also offer repair services and occasionally sell used goods. | 215 | retail.consumer\_electronics |
| Retail Other          | A retail business not currently defined by the taxonomy. | 216 | retail.other |
| Sporting Goods        | An establishment that specializes in selling new sporting equipment, apparel, and related accessories. | 217 | retail.sporting\_goods |
| Pet Store             | An establishment that sells domestic animals and supplies related to their care, like food, toys, and accessories. | 218 | retail.pet\_stores |
| Office Supply         | An establishment that sells domestic animals and supplies related to their care, like food, toys, and accessories. | 219 | retail.office\_supply |
| Home Renovation       | An establishment that sells a wide range of products for home improvement, repair, and decoration. A home renovation store, also known as a home improvement center or home center. | 220 | retail.home\_renovation|

### Outdoor

| Child Category | Category Definition                             | Enumeration ID | String Value (Deprecated) |
| -------------- | ----------------------------------------------- | -------------- | ------------------------- |
| Billboards     | Located primarily on major roads, they attract high-density consumer exposure (mostly to vehicular traffic, but often to pedestrians). | 301 | outdoor.billboards |
| Urban Panels   | Digital screens in urban environments, typically providing a public amenity. Typically visible to pedestrians and in some cases, vehicular traffic as well. | 302 | outdoor.urban\_panels  |
| Bus Shelters   | Enclosures where individuals may wait for buses in an urban environment. Signage may be attached to the interior or exterior of the enclosure.       | 303            | outdoor.bus\_shelters  |
| Spectaculars   | A bulletin that is usually larger than 14’ x 48’ and is positioned at a prime location in a market. A spectacular often utilizes special embellishments.       | 304            | outdoor.spectaculars  |
| Window Panels   | An exterior facing digital display located either in front of or directly behind the window or the exterior wall of a building. Typically visible to pedestrians and in some cases, vehicular traffic as well.       | 305            | outdoor.window\_panel  |
| Moving Billboards   | A digital display appended to or built into the sides and/or back of a vehicle or boat visible to nearby pedestrians and drivers.       | 306            | outdoor.moving\_billboards  |
| Car Tops   | Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers.       | 307            | outdoor.car\_tops  |
| Aerial   | Advertising displays that are flown in the sky.       | 308            | outdoor.aerial  |
| EV Charging Station   | A digital display associated with a piece of infrastructure that allows electric vehicles to recharge their batteries.       | 309            | outdoor.ev\_charging\_station  |

### Health & Beauty

| Child Category | Category Definition                         | Enumeration ID | String Value (Deprecated) |
| -------------- | ------------------------------------------- | -------------- | ------------------------- |
| Gyms           | A club, building, or large room, usually containing special equipment, where people go to do physical exercise and get fit. | 401 | health\_beauty.gyms |
| Salons         | An establishment where a hairdresser, beautician, or couturier conducts business. | 402 | health\_beauty.salons |
| Spas           | A commercial establishment offering health and beauty treatment through such means as steam baths, exercise equipment, and massage. | 403 | health\_beauty.spas   |
| Tattoo           | An establishment in which tattooing is carried out professionally. | 404 | health\_beauty.tattoo   |

### Point of Care

| Child Category     | Category Definition                         | Enumeration ID | String Value (Deprecated) |
| ------------------ | ------------------------------------------- | -------------- | ------------------------- |
| Doctor’s Offices   | Non-hospital facility run by a physician - for treatment of people. | 501 | point\_care.doctor\_offices |
| Veterinary Offices | Non-hopsital facility run by a veterinarian - for treatment of animals. | 502 | point\_care.veterinary\_offices  |
| Dentist Offices    | A place where dental professionals practice dentistry and offer oral health care to patients. | 503 | point\_care.dentist\_offices  |
| Hospitals          | An institution providing medical and surgical treatment and nursing care for sick or injured people. | 504 | point\_care.hospitals  |
| Urgent Care        | A medical facility or clinic that provides prompt treatment for illnesses and injuries that aren't life-threatening. | 505 | point\_care.urgent\_care  |
| Physiotherapy      | A healthcare facility who focuses on restoring movement and function after injury, illness, or disability. | 506 | point\_care.physiotherapy  |

### Education

| Child Category            | Category Definition                            | Enumeration ID | String Value (Deprecated) |
| ------------------------- | ---------------------------------------------- | -------------- | ------------------------- |
| Schools                   | An educational institution designed to provide learning spaces and learning environments for the teaching of students between K - 12 under the direction of teachers. | 601 | education.schools |
| Colleges and Universities | An education institution designed for instruction, examination, or both, of students  in many branches of advanced learning, conferring degrees in various faculties, and often embodying colleges and similar institutions. | 602 | education.colleges |

### Office Buildings

| Child Category   | Category Definition                         | Enumeration ID | String Value (Deprecated) |
| ---------------- | ------------------------------------------- | -------------- | ------------------------- |
| Office Buildings | An office building, also known as an office block or business center is a form of commercial building which contains spaces mainly designed to be used for offices. Advertising displays may be in building lobbies, common areas, or in elevators.     | 701 | office\_buildings.office\_buildings |
| Warehouse | A large building where raw materials or manufactured goods may be stored before their export or distribution for sale.     | 702 | office\_buildings.warehouse |

### Leisure

| Child Category         | Category Definition                            | Enumeration ID | String Value (Deprecated) |
| ---------------------- | ---------------------------------------------- | -------------- | ------------------------- |
| Recreational Locations | Location where recreational and/or leisure activities take place. | 801 | entertainment.recreational |
| Movie Theaters         | Location for displaying long-format content on large screens. | 802 | entertainment.movie\_theaters |
| Sports Entertainment   | A venue that individuals or groups can play an active sport or activity.| 803 | entertainment.sports |
| Bars                   | A retail business that serves alcoholic beverages. | 804 | entertainment.bars |
| Casual Dining          | A restaurant that serves moderately priced food in a casual atmosphere. | 805 | entertainment.casual\_dining |
| QSR                    | A fast food restaurant, also known as a quick service restaurant within the industry, is a specific type of restaurant that serves fast-food cuisine and has minimal table service. | 806            | entertainment.qsr        |
| Hotels                 | An establishment providing accommodations, means, and other services for travelers and tourists.                     | 807            | entertainment.hotels     |
| Golf Carts             | A small motorized vehicle for golfers and their equipment.      | 808            | entertainment.golf\_cart |
| Night Clubs            | An establishment for nighttime entertainment, typically serving drinks and offering music, dancing, etc.   | 809            | entertainment.night\_club |
| High-End Dining        |  (Deprecate) A restaurant that serves expensive food. Often in a more formal atmosphere, and accepting or requiring reservations | 810            | entertainment.high\_end\_dining |
| Casinos                | A public room or building where gambling games are played.   | 811            | entertainment.casino |
| Convention Center      | A large building or complex of buildings designed to host conventions, trade shows, exhibitions, and other large-scale events   | 812            | entertainment.convention\_center |

### Government

| Child Category | Category Definition                                                                                        | Enumeration ID | String Value (Deprecated) |
| -------------- | ---------------------------------------------------------------------------------------------------------- | -------------- | ------------------------- |
| DMVs           | An office building, also known as an office block or business center is a form of commercial building which contains spaces mainly designed to be used for offices. Advertising displays may be in building lobbies, common areas, or in elevators.                          | 901            | government.dmv         |
| Military Bases | A facility that houses and facilitates training for military personnel and operations.                     | 902            | government.military\_bases |
| Post Offices   | A facility that handles the receipt, delivery, and processing of mail, packages, or other postal services. | 903            | government.postal |
| First Responder Facility   | A facility that houses and facilitates training and/or living quarters for Police, Fire, EMS and other first responders | 904            | government.first\_responder\_facility |

### Financial

| Child Category | Category Definition                                                                | Enumeration Value | String Value (Deprecated) |
| -------------- | ---------------------------------------------------------------------------------- | ----------------- | ------------------------- |
| Banks          | A bank is a financial institution licensed to store or invest accountholders money | 1001              | financial.banks           |

### Residential

| Child Category                       | Category Definition                                  | Enumeration Value | String Value (Deprecated) |
| ------------------------------------ | ---------------------------------------------------- | ----------------- | ------------------------- |
| Apartment Buildings and Condominiums | A building that contains different residential units | 1101              | residential.apartment     |

## Grandchild Categories & IDs

### Transit: Airports

| Grandchild Category | Category Definition                                                           | Enumeration ID | String Value (Deprecated)              |
| ------------------- | ----------------------------------------------------------------------------- | -------------- | -------------------------------------- |
| Arrival Hall        | Locations for meeting passengers arriving on flights                          | 10101          | transit.airports.arrivals\_hall        |
| Baggage Claim       | Locations to retrieve baggage not carried during a flight                     | 10102          | transit.airports.baggage\_claim        |
| Departures Hall     | Location for dropping off passengers leaving on flights                       | 10103          | transit.airports.departures\_hall      |
| Food Court          | Location within an airport for food, typically casual                         | 10104          | transit.airports.food\_court           |
| Gates               | Location to wait for or embark or disembark from a specific plane             | 10105          | transit.airports.gates                 |
| Lounges             | (typically private) places to wait for flights, separate from public spaces   | 10106          | transit.airports.lounges               |
| Shopping Area       | Retail areas contained within facilities primarily used for servicing flights | 10107          | transit.airports.shopping\_area        |
| Bar                 | Location within an airport that serves alcoholic beverages. | 10108          | transit.airports.bar        |
| Spectacular         | Large and impactful screen(s) at a prime location. It often utilizes special embellishments | 10109          | transit.airports.spectacular        |

### Transit: Buses

| Grandchild Category | Category Definition                                                       | Enumeration ID | String Value (Deprecated) |
| ------------------- | ------------------------------------------------------------------------- | -------------- | ------------------------- |
| Bus Interior        | Displays located within the interior of city or intercity buses.             | 10201          | transit.buses.bus\_interior         |
| Terminal            | Advertising at facilities for embarking or disembarking from a bus.        | 10202          | transit.buses.terminal    |
| Bus (Outside)       | Displays located on the exterior of city or intercity buses. | 10203          | transit.buses.bus\_exterior |

### Transit: Subway

| Grandchild Category | Category Definition                                                 | Enumeration ID | String Value (Deprecated) |
| ------------------- | ------------------------------------------------------------------- | -------------- | ------------------------- |
| Subway Train Interior       | Advertising displays placed on the interior of subway trains | 10501          | transit.subway.interior     |
| Subway Platform            | Areas to wait for, board, or unboard a subway                       | 10502          | transit.subway.platform   |
| Subway Station             | Displays placed within the concourse areas of a station                       | 10503          | transit.subway.station   |
| Subway Train Exterior      | Advertising displays placed on the exterior of subway trains                      | 10504          | transit.subway.exterior   |
| Subway Spectacular         | Large and impactful screen(s) at a prime location. It often utilizes special embellishments.                       | 10505          | transit.subway.spectacular   |

### Transit: Train Stations

| Grandchild Category | Category Definition                                          | Enumeration ID | String Value (Deprecated)        |
| ------------------- | ------------------------------------------------------------ | -------------- | -------------------------------- |
| Train Interior      | Displays placed in the interior of a railroad or commuter style train       | 10601          | transit.train\_stations.train\_interior    |
| Platform            | Areas to wait for, board, or unboard a train                 | 10602          | transit.train\_stations.platform |
| Train Exterior            | Displays placed on the exterior of a railroad or commuter style train                 | 10603          | transit.train\_stations.train\_exterior|
| Station           | Displays placed within the concourse or exterior areas of a commuter style train station.                 | 10604          | transit.train\_stations.station |
| Spectacular           | Large and impactful screen(s) at a prime location. It often utilizes special embellishments.                 | 10605          | transit.train\_stations.spectacular |

### Transit: Ferry

| Grandchild Category | Category Definition                                          | Enumeration ID | String Value (Deprecated)        |
| ------------------- | ------------------------------------------------------------ | -------------- | -------------------------------- |
| Ferry Interior      | Displays located within the interior of city or intercity ferries       | 10701          | transit.ferry.interior    |
| Ferry Exterior            | Displays located on the exterior of city or intercity ferries                 | 10702          | transit.ferry.exterior |
| Ferry Terminal            | Advertising at facilities for embarking or disembarking from a ferry or boat                 | 10703          | transit.ferry.terminal|


### Transit: Tram

| Grandchild Category | Category Definition                                          | Enumeration ID | String Value (Deprecated)        |
| ------------------- | ------------------------------------------------------------ | -------------- | -------------------------------- |
| Tram Interior      | Displays located within the interior of tram or street cars       | 10801          | transit.tram.interior    |
| Tram Exterior            | Displays located on the exterior of tram or street cars                 | 10802          | transit.tram.exterior |
| Tram Station            | Advertising at facilities for embarking or disembarking from a tram or streetcar                 | 10803          | transit.tram.terminal|

### Transit: Highway Rest Area

| Grandchild Category | Category Definition                                          | Enumeration ID | String Value (Deprecated)        |
| ------------------- | ------------------------------------------------------------ | -------------- | -------------------------------- |
| Exterior      | Displays located outside of any service buildings within the confines of a rest area       | 10901          | transit.highway\_rest\_area.exterior    |
| Concourse            | Displays located with the pedestrian concourse of a rest area, typically interior atrium or hallway type areas                 | 10902          | transit.highway\_rest\_area.concourse  |
| Food Court            | A Common area with multiple food vendors and common tables.                 | 10903          | transit.highway\_rest\_area.food\_court |
| Restroom           | Displays within the restrooms of a highway rest area                | 10904          | transit.highway\_rest\_area.restroom  |

### Retail: Fueling Stations

| Grandchild Category | Category Definition                                                              | Enumeration ID | String Value (Deprecated)  |
| ------------------- | -------------------------------------------------------------------------------- | -------------- | -------------------------- |
| Fuel Dispenser      | A (typically self-service) device for dispensing fuel to vehicles.               | 20101          | retail.gas\_stations.pump  |
| Shop                | A store attached to a location who's primary audience is people fueling vehicles | 20102          | retail.gas\_stations.shop  |

### Retail: Convenience Store

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 20201          | retail.convenience\_store.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 20202          | retail.convenience\_store.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 20203          | retail.convenience\_store.aisles         |
| Exterior             | Area on or near the outside of the building                 | 20204          | retail.convenience\_store.exterior        |

### Retail: Grocery

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 20301          | retail.grocery.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 20302          | retail.grocery.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 20303          | retail.grocery.aisles         |
| Exterior             | Area on or near the outside of the building                 | 20304          | retail.grocery.exterior         |

### Retail: Liquor Stores

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 20401          | retail.liquor\_stores.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 20402          | retail.liquor\_stores.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 20403          | retail.liquor\_stores.aisles         |
| Exterior             | Area on or near the outside of the building                 | 20404          | retail.liquor\_stores.exterior        |

### Retail: Malls

| Grandchild Category | Category Definition                                         | Enumeration ID | String Value (Deprecated) |
| ------------------- | ----------------------------------------------------------- | -------------- | ------------------------- |
| Concourse           | A large open area (including hallways and escalators)       | 20501          | retail.malls.concourse    |
| Food Court          | A Common area with multiple food vendors and common tables. | 20502          | retail.malls.food\_court  |
| Spectacular         | Large and impactful screen(s) at a prime location. It often utilizes special embellishments. | 20503 | retail.malls.spectacular |

### Retail: Pharmacies

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 20701          | retail.pharmacies.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 20702          | retail.pharmacies.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 20703          | retail.pharmacies.aisles         |
| Exterior             | Area on or near the outside of the building                 | 20704          | retail.pharmacies.exterior        |

### Retail: Apparel

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 21001          | retail.apparel.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 21002          | retail.apparel.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 21003          | retail.apparel.aisles         |
| Exterior             | Area on or near the outside of the building                 | 21004          | retail.apparel.exterior        |

### Retail: Vape Shop

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 21301          | retail.vape\_shop.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 21302          | retail.vape\_shop.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 21303          | retail.vape\_shop.aisles         |
| Exterior             | Area on or near the outside of the building                | 21304          | retail.vape\_shop.exterior        |

### Retail: Mass Merchandising

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 21401          | retail.mass\_merchandising.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 21402          | retail.mass\_merchandising.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 21403          | retail.mass\_merchandising.aisles         |
| Exterior             | Area on or near the outside of the building                 | 21404          | retail.mass\_merchandising.exterior        |

### Retail: Consumer Electronics

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 21501          | retail.consumer\_electronics.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 21502          | retail.consumer\_electronics.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 21503          | retail.consumer\_electronics.aisles         |
| Exterior             | Area on or near the outside of the building                 | 21504          | retail.consumer\_electronics.exterior        |

### Retail: Sporting Goods

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 21701          | retail.sporting\_goods.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 21702          | retail.sporting\_goods.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 21703          | retail.sporting\_goods.aisles         |
| Exterior             | Area on or near the outside of the building                 | 21704          | retail.sporting\_goods.exterior        |

### Retail: Pet Stores

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 21801          | retail.pet\_stores.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 21802          | retail.pet\_stores.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 21803          | retail.pet\_stores.aisles         |
| Exterior             | Area on or near the outside of the building                 | 21804          | retail.pet\_stores.exterior        |

### Retail: Office Supply

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 21901          | retail.office\_supply.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 21902          | retail.office\_supply.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 21903          | retail.office\_supply.aisles         |
| Exterior             | Area on or near the outside of the building                | 21904          | retail.office\_supply.exterior        |

### Retail: Home Renovation

| Grandchild Category | Category Definition                                                             | Enumeration ID | String Value (Deprecated)     |
| ------------------- | ------------------------------------------------------------------------------- | -------------- | ----------------------------- |
| Entrance       | Areas near the entrance to a store, often (but not always) visible from outside | 22001          | retail.home\_renovation.entrance |
| Check Out           | Areas primarily dedicated to paying for purchased goods                         | 22002          | retail.home\_renovation.check\_out     |
| Aisles               | Areas primarily dedicated to the display or retrieval of goods                 | 22003          | retail.home\_renovation.aisles         |
| Exterior             | Area on or near the outside of the building                 | 22004          | retail.home\_renovation.exterior        |

### Outdoor: Billboards

| Grandchild Category | Category Definition                                                                                         | Enumeration ID | String Value (Deprecated)       |
| ------------------- | ----------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------- |
| Roadside            | Primarily vehicular environments                                                                            | 30101          | outdoor.billboards.roadside     |
| Highway             | High-speed vehicular environments, typically with controlled entrance/exit (e.g. "exits" or "interchanges") | 30102          | outdoor.billboards.highway      |
| Spectacular         | (DEPRECATE - see child category 304) A bulletin that is usually larger than 14’ x 48’ and is positioned at a prime location in a market. A spectacular often utilizes special embellishments.       | 30103          | outdoor.billboards.spectacular  |

### Outdoor: Aerial

| Grandchild Category | Category Definition                                                                                         | Enumeration ID | String Value (Deprecated)       |
| ------------------- | ----------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------- |
| Aerial Banners         | Advertising display that is carried or pulled behind a flying vehicle (i.e.; helicopter or airplane)       | 30801          | outdoor.billboards.spectacular  |
| Aerial Drones         | Drone light shows that are used to showcase/represent brands and advertising placements       | 30802          | outdoor.billboards.spectacular  |

### Health and Beauty: Gyms

| Grandchild Category | Category Definition                                                           | Enumeration ID | String Value (Deprecated).     |
| ------------------- | ----------------------------------------------------------------------------- | -------------- | ------------------------------ |
| Lobby               | Area for waiting or meeting guests                                            | 40101          | health\_beauty.gyms.lobby.     |
| Fitness Equipment   | Area primarily for exercise or the usage of fitness equipment                 | 40102          | health\_beauty.gyms.equipment  |

### Health and Beauty: Salons (DEPRECATE - use child category 402)

| Grandchild Category  | Category Definition                      | Enumeration ID | String Value (Deprecated).     |
| -------------------- | ---------------------------------------- | -------------- | ------------------------------ |
| Unisex Salon         | Salon catering to clients of any sex     | 40201          | health\_beauty.salons.unisex   |
| Men's Salon          | Salon primarily catering towards men     | 40202          | health\_beauty.salons.mens     |
| Women's Salon        | Salon primarily catering towards women   | 40203          | health\_beauty.salons.womens   |

### Education: Colleges and Universities

| Grandchild Category   | Category Definition                                    | Enumeration ID | String Value (Deprecated)               |
| --------------------- | ------------------------------------------------------ | -------------- | --------------------------------------- |
| Residences            | Places where faculty or students live                  | 60201          | education.colleges.residences           |
| Common Areas          | Shared spaces for study, dining, or leisure activities | 60202          | education.colleges.common               |
| Athletic Facilities   | Facillities or stadiums for sporting competition       | 60203          | education.colleges.athletics            |
| Dining                | On campus facility where food is served for students, staff and visitors       | 60204          | education.colleges.dining            |

### Office Buildings: Office Buildings

| Grandchild Category | Category Definition                                                                                      | Enumeration ID | String Value (Deprecated)               |
| ------------------- | -------------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------- |
| Elevator            | Enclosed, Vertical conveyance for people and goods                                                       | 70101          | office\_buildings.office\_buildings.elevator |
| Lobby               | Common space for tenants to meet and greet visitors and guests, typically near entrances                 | 70102          | office\_buildings.office\_buildings.lobby |
| Gym               | Area within an office building that usually contains special equipment, where people go to do physical exercise and get fit.                 | 70103          | office\_buildings.office\_buildings.gym |
| Break Room               | A designated area in a workplace where employees can take breaks, relax, eat, and socialize. It serves as a space away from the main work area, offering a place for employees to de-stress, recharge, and interact with colleagues.                  | 70104          | office\_buildings.office\_buildings.break\_room |

### Leisure: Recreational Locations

| Grandchild Category   | Category Definition | Enumeration ID | String Value (Deprecated)           |
| --------------------- | ------------------- | -------------- | ----------------------------------- |
| Theme Parks           | An amusement park with a unifying setting or idea.               | 80101          | entertainment.recreational.theme\_parks |
| Museums and Galleries | A building in which objects of historical, scientific, artistic, or cultural interest are stored and exhibited. e.g. "the Museum of Modern Art"                 | 80102          | entertainment.recreational.museums\_galleries |
| Concert Venues        | Any location used for a concert or musical performance                | 80103          | entertainment.recreational.concert\_venues    |
| Bowling Alley        | A location where patrons can take part in bowling activities                | 80104          | entertainment.recreational.bowling    |

### Leisure: Movie Theaters

| Grandchild Category | Category Definition | Enumeration ID | String Value (Deprecated)           |
| ------------------- | ------------------- | -------------- | ----------------------------------- |
| Lobby               | A corridor or hall connected with a larger room or series of rooms and used as a passageway or waiting room: such as a large hall serving as a foyer (as of a hotel or theater)                 | 80201          | entertainment.movie\_theaters.lobby          |
| Food Court          | An area within a building (such as a shopping mall) set apart for food concessions.                 | 80202          | entertainment.movie\_theaters.food\_court    |
| On Screen         | An area within a theater where films are displayed on large screens, typically within an auditorium                 | 80203          | entertainment.movie\_theaters.screen    |
| Restroom         | The restroom of a movie theater, a location for displaying long-format content on large screens.                 | 80204          | entertainment.movie\_theaters.restroom    |

### Leisure: Sports Entertainment

| Grandchild Category | Category Definition | Enumeration ID | String Value (Deprecated)            |
| ------------------- | ------------------- | -------------- | ------------------------------------ |
| Sport Arena         | A central area used for sports or other forms of entertainment and surrounded by seats for spectators. | 80301          | entertainment.sports.arena           |
| Club House          | Locker rooms used by an athletic team                 | 80302          | entertainment.sports.club\_house     |

### Leisure: Casual Dining

| Grandchild Category | Category Definition | Enumeration ID | String Value (Deprecated)            |
| ------------------- | ------------------- | -------------- | ------------------------------------ |
| Restroom         | The restroom of a restaurant that serves moderately priced food in a casual atmosphere. | 80501          | entertainment.casual\_dining.restroom           |

### Leisure: Hotels

| Grandchild Category | Category Definition                                                     | Enumeration ID | String Value (Deprecated)            |
| ------------------- | ----------------------------------------------------------------------- | -------------- | ------------------------------------ |
| Lobby               | Commonly accessible shared spaces for guests at a hotel                 | 80701          | entertainment.hotels.lobby           |
| Elevator            | Commonly accessible, enclosed spaces used to move between floors.       | 80702          | entertainment.hotels.elevator        |
| Room                | Locations occupied and restricted to a single guest                     | 80703          | entertainment.hotels.room            |
| Bar                 | An area within a hotel that serves alcoholic beverages                     | 80704          | entertainment.hotels.bar            |
| Gym                 | Area within a hotel that usually contains special equipment, where people go to do physical exercise and get fit.                     | 80705          | entertainment.hotels.gym            |

### Residential: Apartment Buildings and Condominiums

| Grandchild Category | Category Definition | Enumeration ID | String Value (Deprecated)            |
| ------------------- | ------------------- | -------------- | ------------------------------------ |
| Lobby               | A corridor or hall connected with a larger room or series of rooms and used as a passageway or waiting room: such as a large hall serving as a foyer (as of a hotel or theater)                 | 110101         | residential.apartment\_buildings.lobby         |
| Elevator            | Enclosed, Vertical conveyance for people and goods                   | 110102         | residential.apartment\_buildings.elevator      |
| Gym            | Area within a residential building that usually contains special equipment, where people go to do physical exercise and get fit.                   | 110103         | residential.apartment\_buildings.gym      |
