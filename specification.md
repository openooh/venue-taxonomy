Digital Out-of-Home Screen Venue Types
====

## Introduction

The intention of this document is to standardize the list of venue types that represent Digital-Out-of-Home (DOOH) advertising screens within a programmatic OpenRTB 2.5 context. The systematization of DOOH venue types will allow for clearer targeting by media buying platforms across a spectrum of available supply-side platforms offering DOOH inventory.

## Contributors

### About Broadsign

Broadsign is making it easier than ever for media owners, agencies and brands to harness the power of out-of-home and connect with audiences across the globe. Powering over 425,000 signs in airports, shopping malls, health clinics, transit systems and more, Broadsign is at the heart of people’s lives. 

The Broadsign platform helps media owners more efficiently manage their business operations while enabling brands and agencies to easily book OOH campaigns. The platform includes tools for content distribution, playback and proof of performance; sales inventory availability and proposal generation; automated programmatic DOOH transactions; and OOH business operations. 

### About The Trade Desk

The Trade Desk powers the most sophisticated buyers in advertising technology. Founded by the pioneers of real-time bidding, The Trade Desk has become the fastest growing demand-side platform in the industry by offering agencies, aggregators, and their advertisers best-in-class technology to manage display, social, mobile, video, audio, connected TV, and Digital-Out-of-Home advertising campaigns.

The Trade Desk empowers buyers at the campaign level with the most expressive bid capabilities in market, full-funnel attribution, and detailed reporting that gives you more insights into your audience, from initial impression to conversion. By maintaining a pure buy-side focus, The Trade Desk delivers on branding and performance for clients worldwide.

### About Vistar Media

Vistar Media is the world’s leading end-to-end programmatic ecosystem for digital out-of-home (DOOH). Vistar Media’s demand-side platform (DSP) and supply-side platform (SSP) empower buyers and sellers to easily transact on DOOH inventory while applying intelligent data insights that improve media performance. Vistar’s SaaS solutions (unified ad server and Cortex for device and content management) deliver enterprise-grade solutions for monetizing and operating digital signage networks at any scale. Through its global reach, direct platform integrations, data partnerships, and complete technology stack, Vistar Media continues to power innovation and growth across the digital signage industry. Founded in 2012, Vistar Media is headquartered in New York City and has offices across the United States, Canada, the United Kingdom and Australia.

### Individuals

* Alex Cohen, The Trade Desk
* Christian Collins, Vistar Media
* Aura Koljonen, Broadsign
* Eric Lamb, Vistar Media
* Matthew Mercuri, Broadsign

###Versioning

| Version Number | Published    | Acceptance                              |
| -------------- | ---------    | --------------------------------------- |
| 1.0            | June 4, 2020 | Broadsign, The Trade Desk, Vistar Media |

## Getting Started

Digital Out-of-Home screens, available within a programmatic context, maintain specific geospatial and physical parameters that describe the conditions, environment and/or surroundings. These parameters provide a mutual understanding between buyer and seller within the bidstream and during the transaction phase of trading media.This specification clarifies and classifies these parameters to maintain knowledge equality within the DOOH programmatic industry for all parties involved.

## Definitions & Specification Guidelines

Screen Venue Types should describe an environment and the audience that may be found there. 

A venue type should also describe a media format, except when the media format cannot be separated from the environment. For example, an “ATM” may be in a mall, or a convenience store. The venue type should reflect those parameters.

Screen venue types should not obscure key elements of the environment. 

Venue types should not equate environments that serve dramatically different purposes. For example, it would be insincere to label both Marijuana dispensaries AND pharmacies under the “Wellness” category. These two environments serve very different purposes and audiences, and thus cannot be grouped together.

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

`device.ext.dooh.venuetypelist`
`device.ext.dooh.venuetypeid`
`device.ext.dooh.venuetypestring`

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `device.ext.dooh.venuetypeid` | Integer array | List of IDs that describe the venue of the requesting screen | 

## Value Format

The following spec subscribes to UTF-8 encoding.

### Enumeration ID

Each category, regardless of tier, has a unique identifier (ID) that is immutable. DSPs may opt to target this specific ID based on the media they wish to bid on.

### Enumerated List

The enumerated list can be passed in the bid request. It is a comma-separated array of category IDs from the preceding and dependent tiers. Should only a parent-child category be associated with the screen’s venue, the array will be composed of two enumerated IDs. Refer to the summary chart for further details.

### String Values

String values are text-based identifiers of venue categories. Dependencies on parent and child tiers use a period connector for tier separation. All unique text identifiers are lower case, and combination words utilize the standard underscore. String values may be used as substitutions for enumeration values and enumerated lists and provide greater flexibility for implementation.

## Parent Categories & IDs

| Parent Category  | Enumeration ID | String Value     |
| ---------------- | -------------- | ---------------- |
| Transit          | 1              | transit          |
| Retail           | 2              | retail           |
| Outdoor          | 3              | outdoor          |
| Health & Beauty  | 4              | health_beauty    |
| Point of Care    | 5              | point_care       |
| Education        | 6              | education        |
| Office Buildings | 7              | office_buildings |
| Entertainment    | 8              | entertainment    |
| Government       | 9              | government       |
| Financial        | 10             | financial        |
| Residential      | 11             | residential      |

## Child Categories & IDs

### Transit

| Child Category | Category Definition                            | Enumeration ID | String Value               |
| -------------- | ---------------------------------------------- | -------------- | -------------------------- |
| Airports | Signage located throughout terminals in arrival and departure areas, ticketing areas, baggage claim, gate-hold rooms, concourses, retail shops, and VIP lounges. | 101 | transit.airports |
| Buses | Displays located on the inside of city or intercity buses. | 102 | transit.buses |
| Taxi & Rideshare TV  | Advertising displays placed inside taxis and rideshare vehicles visible to passengers in the back seat. | 103 | transit.taxi\_rideshare\_tv |
| Taxi & Rideshare Top | Advertising displays placed on top of taxi and rideshare vehicles visible to nearby pedestrian and drivers. | 104 | transit.taxi\_rideshare\_top |
| Subway | Advertising displays placed inside subway trains or inside stations or on subway platforms. | 105 | transit.subway |
| Train Stations | Advertising displays placed inside train stations or on platforms. | 106 | transit.train\_stations    |

### Retail

| Child Category     | Category Definition                             | Enumeration ID | String Value            |
| ------------------ | ----------------------------------------------- | -------------- | ----------------------- |
|                    |                                                 |                |                         |
| Gas Stations       | An establishment beside a road selling fuel     | 201            | retail.gas\_stations    |
|                    | for motor vehicles.                             |                |                         |
|                    |                                                 |                |                         |
| Convenience Stores | A store with extended opening hours and in a    | 202            | retail.convenience\_sto |
|                    | convenient location, stocking a limited range   |                | re                      |
|                    | of household goods and groceries.               |                |                         |
|                    |                                                 |                |                         |
| Grocery            | A retail shop that primarily sells food, either | 203            | retail.grocery          |
|                    | fresh or preserved.                             |                |                         |
|                    |                                                 |                |                         |
| Liquor Stores      | A retail shop that predominantly sells          | 204            | retail.liquor\_stores   |
|                    | prepackaged alcoholic beverages, typically in   |                |                         |
|                    | bottles, intended to be consumed off the        |                |                         |
|                    | store’s premises.                               |                |                         |
|                    |                                                 |                |                         |
| Mall               | A large building or series of connected         | 205            | retail.malls            |
|                    | buildings containing a variety of retail stores |                |                         |
|                    | and typically also restaurants.                 |                |                         |
|                    |                                                 |                |                         |
| Dispensaries       | A store that sells and dispenses medicinal      | 206            | retail.dispensaries     |
|                    | marijuana and CBD products.                     |                |                         |
|                    |                                                 |                |                         |
| Pharmacies         | A store where medicinal drugs are dispensed     | 207            | retail.pharmacies       |
|                    | and sold.                                       |                |                         |
|                    |                                                 |                |                         |
| Parking Garages    | A building in which people usually pay to       | 208            | retail.parking\_garages |
|                    | park their cars, trucks and other vehicles.     |                |                         |

### Outdoor

| Child Category | Category Definition                             | Enumeration ID | String Value           |
| -------------- | ----------------------------------------------- | -------------- | ---------------------- |
|                |                                                 |                |                        |
| Billboards     | Located primarily on major roads, they attract  | 301            | outdoor.billboards     |
|                | high-density consumer exposure (mostly to       |                |                        |
|                | vehicular traffic, but often to pedestrians).   |                |                        |
|                |                                                 |                |                        |
| Urban Panels   | Digital screens in urban environments,          | 302            | outdoor.billboards.urb |
|                | typically providing a public amenity. Typically |                | an\_panels             |
|                | visible to pedestrians and in some cases,       |                |                        |
|                | vehicular traffic as well.                      |                |                        |
|                |                                                 |                |                        |
| Bus Shelters   | Enclosures where individuals may wait for       | 303            | outdoor.billboards.bus |
|                | buses in an urban environment. Signage          |                | \_shelters             |
|                | may be attached to the interior or exterior of  |                |                        |


### Health & Beauty

| Child Category | Category Definition                         | Enumeration ID | String Value          |
| -------------- | ------------------------------------------- | -------------- | --------------------- |
|                |                                             |                |                       |
| Gyms           | A club, building, or large room, usually    | 401            | health\_beauty.gyms   |
|                | containing special equipment, where people  |                |                       |
|                | go to do physical exercise and get fit.     |                |                       |
|                |                                             |                |                       |
| Salons         | An establishment where a hairdresser,       | 402            | health\_beauty.salons |
|                | beautician, or couturier conducts business. |                |                       |
|                |                                             |                |                       |
| Spas           | A commercial establishment offering health  | 403            | health\_beauty.spas   |
|                | and beauty treatment through such means     |                |                       |
|                | as steam baths, exercise equipment, and     |                |                       |
|                | massage.                                    |                |                       |
|                |                                             |                |                       |

### Point of Care

| Child Category     | Category Definition                         | Enumeration ID | String Value              |
| ------------------ | ------------------------------------------- | -------------- | ------------------------- |
|                    |                                             |                |                           |
| Doctor’s Offices   | A club, building, or large room, usually    | 501            | point\_care.doctor\_offic |
|                    | containing special equipment, where people  |                | es                        |
|                    | go to do physical exercise and get fit.     |                |                           |
|                    |                                             |                |                           |
| Veterinary Offices | An establishment where a hairdresser,       | 502            | point\_care.veterinary\_  |
|                    | beautician, or couturier conducts business. |                | offices                   |

### Education

| Child Category            | Category Definition                            | Enumeration ID | String Value       |
| ------------------------- | ---------------------------------------------- | -------------- | ------------------ |
|                           |                                                |                |                    |
| Schools                   | An educational institution designed to         | 601            | education.schools  |
|                           | provide learning spaces and learning           |                |                    |
|                           | environments for the teaching of students      |                |                    |
|                           | between K - 12 under the direction of          |                |                    |
|                           | teachers.                                      |                |                    |
|                           |                                                |                |                    |
| Colleges and Universities | An education institution designed for          | 602            | education.colleges |
|                           | instruction, examination, or both, of students |                |                    |
|                           | in many branches of advanced learning,         |                |                    |
|                           | conferring degrees in various faculties, and   |                |                    |
|                           | often embodying colleges and similar           |                |                    |
|                           | institutions.                                  |                |                    |

### Office Buildings

| Child Category   | Category Definition                         | Enumeration ID | String Value               |
| ---------------- | ------------------------------------------- | -------------- | -------------------------- |
|                  |                                             |                |                            |
| Office Buildings | An office building, also known as an office | 701            | office\_buildings.office\_ |
|                  | block or business center is a form of       |                | buildings                  |
|                  | commercial building which contains spaces   |                |                            |
|                  | mainly designed to be used for offices.     |                |                            |
|                  | Advertising displays may be in building     |                |                            |
|                  | lobbies, common areas, or in elevators.     |                |                            |

### Entertainment

| Child Category         | Category Definition                            | Enumeration ID | String Value             |
| ---------------------- | ---------------------------------------------- | -------------- | ------------------------ |
|                        |                                                |                |                          |
| Recreational Locations | An educational institution designed to         | 801            | entertainment.recreati   |
|                        | provide learning spaces and learning           |                | onal                     |
|                        | environments for the teaching of students      |                |                          |
|                        | between K - 12 under the direction of          |                |                          |
|                        | teachers.                                      |                |                          |
|                        |                                                |                |                          |
| Movie Theaters         | An education institution designed for          | 802            | entertainment.movie\_t   |
|                        | instruction, examination, or both, of students |                | heaters                  |
|                        | in many branches of advanced learning,         |                |                          |
|                        | conferring degrees in various faculties, and   |                |                          |
|                        | often embodying colleges and similar           |                |                          |
|                        | institutions.                                  |                |                          |
|                        |                                                |                |                          |
| Sports Entertainment   | A venue that individuals or groups can play    | 803            | entertainment.sports     |
|                        | an active sport or activity.                   |                |                          |
| Bars                   | A retail business that serves alcoholic        | 804            | entertainment.bars       |
|                        | beverages.                                     |                |                          |
|                        |                                                |                |                          |
| Casual Dining          | A restaurant that serves moderately priced     | 805            | entertainment.casual\_   |
|                        | food in a casual atmosphere.                   |                | dining                   |
|                        |                                                |                |                          |
| QSR                    | A fast food restaurant, also known as a quick  | 806            | entertainment.qsr        |
|                        | service restaurant within the industry, is a   |                |                          |
|                        | specific type of restaurant that serves        |                |                          |
|                        | fast-food cuisine and has minimal table        |                |                          |
|                        | service.                                       |                |                          |
|                        |                                                |                |                          |
| Hotels                 | An establishment providing                     | 807            | entertainment.hotels     |
|                        | accommodations, means, and other services      |                |                          |
|                        | for travelers and tourists.                    |                |                          |
|                        |                                                |                |                          |
| Golf Carts             | A small motorized vehicle for golfers and      | 808            | entertainment.golf\_cart |
|                        | their equipment.                               |                | s                        |

### Government

| Child Category | Category Definition                             | Enumeration ID | String Value           |
| -------------- | ----------------------------------------------- | -------------- | ---------------------- |
|                |                                                 |                |                        |
| DMVs           | An office building, also known as an office     | 901            | government.dmv         |
|                | block or business center is a form of           |                |                        |
|                | commercial building which contains spaces       |                |                        |
|                | mainly designed to be used for offices.         |                |                        |
|                | Advertising displays may be in building         |                |                        |
|                | lobbies, common areas, or in elevators.         |                |                        |
|                |                                                 |                |                        |
| Military Bases | A facility that houses and facilitates training | 902            | government.military\_b |
|                | for military personnel and operations.          |                | ases                   |

### Financial

| Child Category | Category Definition                           | Enumeration Value | String Value    |
| -------------- | --------------------------------------------- | ----------------- | --------------- |
|                |                                               |                   |                 |
| Banks          | A bank is a financial institution licensed to | 1001              | financial.banks |

### Residential

| Child Category      | Category Definition                            | Enumeration Value | String Value          |
| ------------------- | ---------------------------------------------- | ----------------- | --------------------- |
|                     |                                                |                   |                       |
| Apartment Buildings | A building that contains different residential | 1101              | residential.apartment |

## Grandchild Categories & IDs

### Transit: Airports

| Grandchild Category | Category Definition | Enumeration ID | String Value              |
| ------------------- | ------------------- | -------------- | ------------------------- |
|                     |                     |                |                           |
| Arrival Hall        | TBC                 | 10101          | transit.airports.arrivals |
|                     |                     |                | \_hall                    |
|                     |                     |                |                           |
| Baggage Claim       | TBC                 | 10102          | transit.airports.baggag   |
|                     |                     |                | e\_claim                  |
|                     |                     |                |                           |
| Departures Hall     | TBC                 | 10103          | transit.airports.departu  |
|                     |                     |                | res\_hall                 |
|                     |                     |                |                           |
| Food Court          | TBC                 | 10104          | transit.airports.food\_co |
|                     |                     |                | urt                       |
|                     |                     |                |                           |
| Gates               | TBC                 | 10105          | transit.airports.gates    |
|                     |                     |                |                           |
| Lounges             | TBC                 | 10106          | transit.airports.lounges  |
|                     |                     |                |                           |
| Shopping Area       | TBC                 | 10107          | transit.airports.shoppin  |
|                     |                     |                | g\_area                   |

### Transit: Buses

| Grandchild Category | Category Definition | Enumeration ID | String Value           |
| ------------------- | ------------------- | -------------- | ---------------------- |
|                     |                     |                |                        |
| Bus                 | TBC                 | 10201          | transit.buses.bus      |
|                     |                     |                |                        |
| Terminal            | TBC                 | 10202          | transit.buses.terminal |

### Transit: Subway

| Grandchild Category | Category Definition | Enumeration ID | String Value            |
| ------------------- | ------------------- | -------------- | ----------------------- |
|                     |                     |                |                         |
| Subway Train        | TBC                 | 10501          | transit.subway.train    |
|                     |                     |                |                         |
| Platform            | TBC                 | 10502          | transit.subway.platform |

### Transit: Train Stations

| Grandchild Category | Category Definition | Enumeration ID | String Value                    |
| ------------------- | ------------------- | -------------- | ------------------------------- |
| Train               | TBC                 | 10601          | transit.train\_stations.train   |
| Platform            | TBC                 | 10602          | transit.train\_station.platform |

### Retail: Gas Stations

| Grandchild Category | Category Definition | Enumeration ID | String Value               |
| ------------------- | ------------------- | -------------- | -------------------------- |
|                     |                     |                |                            |
| Pump                | TBC                 | 20101          | retail.gas\_stations.pump  |
|                     |                     |                | mp                         |
|                     |                     |                |                            |
| Shop                | TBC                 | 20102          | retail.gas\_stations.shop  |

### Retail: Grocery

| Grandchild Category | Category Definition | Enumeration ID | String Value                  |
| ------------------- | ------------------- | -------------- | ----------------------------- |
|                     |                     |                |                               |
| Shop Entrance       | TBC                 | 20301          | retail.grocery.shop\_entrance |
| Check Out           | TBC                 | 20302          | retail.grocery.check\_out     |

### Retail: Malls

| Grandchild Category | Category Definition | Enumeration ID | String Value             |
| ------------------- | ------------------- | -------------- | ------------------------ |
|                     |                     |                |                          |
| Concourse           | TBC                 | 20501          | retail.malls.concourse   |
|                     |                     |                |                          |
| Food Court          | TBC                 | 20502          | retail.malls.food\_court |
|                     |                     |                |                          |
| Spectacular         | TBC                 | 20503          | retail.malls.spectacular |

### Outdoor: Billboards

| Grandchild Category | Category Definition | Enumeration ID | String Value            |
| ------------------- | ------------------- | -------------- | ----------------------- |
|                     |                     |                |                         |
| Roadside            | TBC                 | 30101          | outdoor.billboards.roa  |
|                     |                     |                | dside                   |
|                     |                     |                |                         |
| Highway             | TBC                 | 30102          | outdoor.billboards.high |
|                     |                     |                | way                     |
|                     |                     |                |                         |
| Spectacular         | TBC                 | 30103          | outdoor.billboards.spe  |
|                     |                     |                | ctacular                |

### Health and Beauty: Gyms

| Grandchild Category | Category Definition | Enumeration ID | String Value           |
| ------------------- | ------------------- | -------------- | ---------------------- |
|                     |                     |                |                        |
| Lobby               | TBC                 | 40101          | health\_beauty.gyms.lo |
|                     |                     |                | bby                    |
|                     |                     |                |                        |
| Fitness Equipment   | TBC                 | 40102          | health\_beauty.gyms.e  |
|                     |                     |                | quipment               |

### Office Buildings: Office Buildings

| Grandchild Category | Category Definition | Enumeration ID | String Value               |
| ------------------- | ------------------- | -------------- | -------------------------- |
|                     |                     |                |                            |
| Elevator            | TBC                 | 70101          | office\_buildings.office\_ |
|                     |                     |                | buildings.elevator         |
|                     |                     |                |                            |
| Lobby               | TBC                 | 70102          | office\_buildings.office\_ |
|                     |                     |                | buildings.lobby            |

### Entertainment: Recreational Locations

| Grandchild Category   | Category Definition | Enumeration ID | String Value           |
| --------------------- | ------------------- | -------------- | ---------------------- |
|                       |                     |                |                        |
| Theme Parks           | TBC                 | 80101          | entertainment.recreati |
|                       |                     |                |                        |
| Museums and Galleries | TBC                 | 80102          | entertainment.recreati |
|                       |                     |                | onal.museums\_galleri  |
|                       |                     |                | es                     |
|                       |                     |                |                        |
| Concert Venues        | TBC                 | 80103          | entertainment.recreati |
|                       |                     |                | onal.concer\_venues    |

### Entertainment: Movie Theaters

| Grandchild Category | Category Definition | Enumeration ID | String Value           |
| ------------------- | ------------------- | -------------- | ---------------------- |
|                     |                     |                |                        |
| Lobby               | TBC                 | 80201          | entertainment.movie\_t |
|                     |                     |                | heaters.lobby          |
|                     |                     |                |                        |
| Food Court          | TBC                 | 80202          | entertainment.movie\_t |
|                     |                     |                | heaters.food\_court    |

### Entertainment: Sports Entertainment

| Grandchild Category | Category Definition | Enumeration ID | String Value            |
| ------------------- | ------------------- | -------------- | ----------------------- |
|                     |                     |                |                         |
| Sport Arena         | TBC                 | 80301          | entertainment.sports.a  |
|                     |                     |                | rena                    |
|                     |                     |                |                         |
| Club House          | TBC                 | 80302          | entertainment.sports.cl |
|                     |                     |                | ub\_house               |

### Entertainment: Hotels

| Grandchild Category | Category Definition | Enumeration ID | String Value            |
| ------------------- | ------------------- | -------------- | ----------------------- |
|                     |                     |                |                         |
| Lobby               | TBC                 | 80701          | entertainment.hotels.lo |
|                     |                     |                | bby                     |
|                     |                     |                |                         |
| Elevator            | TBC                 | 80702          | entertainment.hotels.el |
|                     |                     |                | evator                  |

### Residential: Apartment Buildings

| Grandchild Category | Category Definition | Enumeration ID | String Value            |
| ------------------- | ------------------- | -------------- | ----------------------- |
| Lobby               | TBC                 | 110101         | residential.apartment\_ |
|                     |                     |                | buildings.lobby         |
|                     |                     |                |                         |
| Elevator            | TBC                 | 110102         | residential.apartment\_ |
|                     |                     |                | buildings.elevator      |

## Summary Table

| Parent            | Child              | Grandchild        | Enumeration | Enumeration          | String                 |
| ----------------- | ------------------ | ----------------- | ----------- | -------------------- | ---------------------- |
| Category          | Category           | Category          | ID          | Array                | List                   |
|                   |                    |                   |             |                      |                        |
| Transit           | \-                 | \-                | 1           | \[1\]                | transit                |
|                   |                    |                   |             |                      |                        |
| Transit           | Airports           | \-                | 101         | \[1, 101\]           | transit.airports       |
|                   |                    |                   |             |                      |                        |
| Transit           | Airports           | Arrivals Hall     | 10101       | \[1, 101, 10101\]    | transit.airports.arri  |
|                   |                    |                   |             |                      | vals\_hall             |
|                   |                    |                   |             |                      |                        |
| Transit           | Airports           | Baggage Claim     | 10102       | \[1, 101, 10102\]    | transit.airports.bag   |
|                   |                    |                   |             |                      | gage\_claim            |
|                   |                    |                   |             |                      |                        |
| Transit           | Airports           | Departures Hall   | 10103       | \[1, 101, 10103\]    | transit.airports.dep   |
|                   |                    |                   |             |                      | artures\_hall          |
|                   |                    |                   |             |                      |                        |
| Transit           | Airports           | Food Court        | 10104       | \[1, 101, 10104\]    | transit.airports.foo   |
|                   |                    |                   |             |                      | d\_court               |
|                   |                    |                   |             |                      |                        |
| Transit           | Airports           | Gates             | 10105       | \[1, 101, 10105\]    | transit.airports.gat   |
|                   |                    |                   |             |                      | es                     |
|                   |                    |                   |             |                      |                        |
| Transit           | Airports           | Lounges           | 10106       | \[1, 101, 10106\]    | transit.airports.lou   |
|                   |                    |                   |             |                      | nges                   |
|                   |                    |                   |             |                      |                        |
| Transit           | Airports           | Shopping Area     | 10107       | \[1, 101, 10107\]    | transit.airports.sho   |
|                   |                    |                   |             |                      | pping\_area            |
|                   |                    |                   |             |                      |                        |
| Transit           | Buses              | \-                | 102         | \[1, 102\]           | transit.buses          |
|                   |                    |                   |             |                      |                        |
| Transit           | Buses              | Bus               | 10201       | \[1, 102, 10201\]    | transit.buses.bus      |
|                   |                    |                   |             |                      |                        |
| Transit           | Buses              | Terminal          | 10202       | \[1, 102, 10202\]    | transit.buses.termi    |
| Transit           | Taxi & Rideshare   | \-                | 103         | \[1, 103\]           | transit.taxi\_ridesha  |
|                   | TV                 |                   |             |                      | re\_tv                 |
|                   |                    |                   |             |                      |                        |
| Transit           | Taxi & Rideshare   | \-                | 104         | \[1, 104\]           | transit.taxi\_ridesha  |
|                   | Top                |                   |             |                      | re\_top                |
|                   |                    |                   |             |                      |                        |
| Transit           | Subway             | \-                | 105         | \[1, 105\]           | transit.subway         |
|                   |                    |                   |             |                      |                        |
| Transit           | Subway             | Subway Train      | 10501       | \[1, 105, 10501\]    | transit.subway.trai    |
|                   |                    |                   |             |                      | n                      |
|                   |                    |                   |             |                      |                        |
| Transit           | Subway             | Platform          | 10502       | \[1, 105, 10502\]    | transit.subway.plat    |
|                   |                    |                   |             |                      | form                   |
|                   |                    |                   |             |                      |                        |
| Transit           | Train Stations     | \-                | 106         | \[1, 106\]           | transit.train\_statio  |
|                   |                    |                   |             |                      | ns                     |
|                   |                    |                   |             |                      |                        |
| Transit           | Train Stations     | Train             | 10601       | \[1, 106, 10601\]    | transit\_train\_statio |
|                   |                    |                   |             |                      | ns.train               |
|                   |                    |                   |             |                      |                        |
| Transit           | Train Stations     | Platform          | 10602       | \[1, 106, 10602\]    | transit\_train\_statio |
|                   |                    |                   |             |                      | ns.platform            |
|                   |                    |                   |             |                      |                        |
| Retail            | \-                 | \-                | 2           | \[2\]                | retail                 |
|                   |                    |                   |             |                      |                        |
| Retail            | Gas Station        | \-                | 201         | \[2, 201\]           | retail.gas\_stations   |
|                   |                    |                   |             |                      |                        |
| Retail            | Gas Station        | Pump              | 20101       | \[2, 201, 20101\]    | retail.gas\_stations.  |
|                   |                    |                   |             |                      | pump                   |
|                   |                    |                   |             |                      |                        |
| Retail            | Gas Station        | Shop              | 20102       | \[2, 201, 20102\]    | retail.gas\_stations.  |
|                   |                    |                   |             |                      | shop                   |
|                   |                    |                   |             |                      |                        |
| Retail            | Convenience        | \-                | 202         | \[2, 202\]           | retail.convenience     |
|                   | Stores             |                   |             |                      | \_store                |
|                   |                    |                   |             |                      |                        |
| Retail            | Grocery            | \-                | 203         | \[2, 203\]           | retail.grocery         |
|                   |                    |                   |             |                      |                        |
| Retail            | Grocery            | Shop Entrance     | 20301       | \[2, 203, 20301\]    | retail.grocery.shop    |
|                   |                    |                   |             |                      | \_entrance             |
|                   |                    |                   |             |                      |                        |
| Retail            | Grocery            | Check Out         | 20302       | \[2, 203, 20302\]    | retail.grocery.chec    |
|                   |                    |                   |             |                      | k\_out                 |
|                   |                    |                   |             |                      |                        |
| Retail            | Liquor Stores      | \-                | 204         | \[2, 204\]           | retail.liquor\_stores  |
|                   |                    |                   |             |                      |                        |
| Retail            | Malls              | \-                | 205         | \[2, 205\]           | retail.malls           |
|                   |                    |                   |             |                      |                        |
| Retail            | Malls              | Concourse         | 20501       | \[2, 205, 20501\]    | retail.malls.concou    |
|                   |                    |                   |             |                      | rse                    |
|                   |                    |                   |             |                      |                        |
| Retail            | Malls              | Food Court        | 20502       | \[2, 205, 20502\]    | retail.malls.food\_c   |
|                   |                    |                   |             |                      | ourt                   |
|                   |                    |                   |             |                      |                        |
| Retail            | Malls              | Spectacular       | 20503       | \[2, 205, 20503\]    | retail.malls.specta    |
|                   |                    |                   |             |                      | cular                  |
|                   |                    |                   |             |                      |                        |
| Retail            | Dispensaries       | \-                | 206         | \[2, 206\]           | retail.dispensaries    |
|                   |                    |                   |             |                      |                        |
| Retail            | Pharmacies         | \-                | 207         | \[2, 207\]           | retail.pharmacies      |
|                   |                    |                   |             |                      |                        |
| Retail            | Parking Garages    | \-                | 208         | \[2, 208\]           | retail.parking\_gara   |
|                   |                    |                   |             |                      | ges                    |
|                   |                    |                   |             |                      |                        |
| Outdoor           | \-                 | \-                | 3           | \[3\]                | outdoor                |
|                   |                    |                   |             |                      |                        |
| Outdoor           | Billboard          | \-                | 301         | \[3, 301\]           | outdoor.billboards     |
|                   |                    |                   |             |                      |                        |
| Outdoor           | Billboard          | Roadside          | 30101       | \[3, 301, 30101\]    | outdoor.billboards.    |
|                   |                    |                   |             |                      | roadside               |
|                   |                    |                   |             |                      |                        |
| Outdoor           | Billboard          | Highway           | 30102       | \[3, 301, 30102\]    | outdoor.billboards.    |
| Outdoor           | Billboard          | Spectacular       | 30103       | \[3, 301, 30103\]    | outdoor.billboards.    |
|                   |                    |                   |             |                      | spectacular            |
|                   |                    |                   |             |                      |                        |
| Outdoor           | Urban Panels       | \-                | 302         | \[3, 302\]           | outdoor.urban\_pa      |
|                   |                    |                   |             |                      | nels                   |
|                   |                    |                   |             |                      |                        |
| Outdoor           | Bus Shelters       | \-                | 303         | \[3, 303\]           | outdoor.bust\_shelt    |
|                   |                    |                   |             |                      | ers                    |
|                   |                    |                   |             |                      |                        |
| Health and Beauty | \-                 | \-                | 4           | \[4\]                | health\_beauty         |
|                   |                    |                   |             |                      |                        |
| Health and Beauty | Gyms               | \-                | 401         | \[4, 401\]           | health\_beauty.gy      |
|                   |                    |                   |             |                      | ms                     |
|                   |                    |                   |             |                      |                        |
| Health and Beauty | Gyms               | Lobby             | 40101       | \[4, 401, 40101\]    | health\_beauty.gy      |
|                   |                    |                   |             |                      | ms.lobby               |
|                   |                    |                   |             |                      |                        |
| Health and Beauty | Gyms               | Fitness Equipment | 40102       | \[4, 401, 40102\]    | health\_beauty.gy      |
|                   |                    |                   |             |                      | ms.equipment           |
|                   |                    |                   |             |                      |                        |
| Health and Beauty | Salons             | \-                | 402         | \[4, 402\]           | health\_beauty.salo    |
|                   |                    |                   |             |                      | ns                     |
|                   |                    |                   |             |                      |                        |
| Health and Beauty | Spas               | \-                | 403         | \[4, 403\]           | health\_beauty.spa     |
|                   |                    |                   |             |                      | s                      |
|                   |                    |                   |             |                      |                        |
| Point of Care     | \-                 | \-                | 5           | \[5\]                | point\_care            |
|                   |                    |                   |             |                      |                        |
| Point of Care     | Doctor’s Offices   | \-                | 501         | \[5, 501\]           | point\_care.doctor\_   |
|                   |                    |                   |             |                      | offices                |
|                   |                    |                   |             |                      |                        |
| Point of Care     | Veterinary Offices | \-                | 502         | \[5, 502\]           | point\_care.veterin    |
|                   |                    |                   |             |                      | ary\_offices           |
|                   |                    |                   |             |                      |                        |
| Education         | \-                 | \-                | 6           | \[6\]                | education              |
|                   |                    |                   |             |                      |                        |
| Education         | Schools            | \-                | 601         | \[6, 601\]           | education.schools      |
|                   |                    |                   |             |                      |                        |
| Education         | Colleges and       | \-                | 602         | \[6, 602\]           | education.colleges     |
|                   | Universities       |                   |             |                      |                        |
|                   |                    |                   |             |                      |                        |
| Office Buildings  | \-                 | \-                | 7           | \[7\]                | office\_buildings      |
|                   |                    |                   |             |                      |                        |
| Office Buildings  | Office Buildings   | \-                | 701         | \[7, 701\]           | office\_buildings.off  |
|                   |                    |                   |             |                      | ice\_buildings         |
|                   |                    |                   |             |                      |                        |
| Office Buildings  | Office Buildings   | Elevator          | 70101       | \[7, 701, 70101\]    | office\_buildings.off  |
|                   |                    |                   |             |                      | ice\_buildings.elev    |
|                   |                    |                   |             |                      | ator                   |
|                   |                    |                   |             |                      |                        |
| Office Buildings  | Office Buildings   | Lobby             | 70102       | \[7, 701, 70102\]    | office\_buildings.off  |
|                   |                    |                   |             |                      | ice\_buildings.lobb    |
|                   |                    |                   |             |                      | y                      |
|                   |                    |                   |             |                      |                        |
| Entertainment     | \-                 | \-                | 8           | \[8\]                | entertainment          |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Recreational       | \-                | 801         | \[8, 801\]           | entertainment.recr     |
|                   | Locations          |                   |             |                      | eational               |
| Entertainment     | Recreational       | Theme Parks       | 80101       | \[8, 801, 80101\]    | entertainment.recr     |
|                   | Locations          |                   |             |                      | eational.theme\_pa     |
|                   |                    |                   |             |                      | rks                    |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Recreational       | Museums and       | 80102       | \[8, 801, 80102\]    | entertainment.recr     |
|                   | Locations          | Galleries         |             |                      | eational.museums       |
|                   |                    |                   |             |                      | \_galleries            |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Recreational       | Concert Venues    | 80103       | \[8, 801, 80103\]    | entertainment.recr     |
|                   | Locations          |                   |             |                      | eational.concert\_v    |
|                   |                    |                   |             |                      | enues                  |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Movie Theaters     | \-                | 802         | \[8, 802\]           | entertainment.mov      |
|                   |                    |                   |             |                      | ie\_theaters           |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Movie Theaters     | Lobby             | 80201       | \[8, 802, 80201\]    | entertainment.mov      |
|                   |                    |                   |             |                      | ie\_theaters.lobby     |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Movie Theaters     | Food Court        | 80202       | \[8, 802, 80202\]    | entertainment.mov      |
|                   |                    |                   |             |                      | ie\_theaters.food\_c   |
|                   |                    |                   |             |                      | ourt                   |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Sports             | \-                | 803         | \[8, 803\]           | entertainment.spor     |
|                   | Entertainment      |                   |             |                      | ts                     |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Sports             | Sport Arena       | 80301       | \[8, 803, 80301\]    | entertainment.spor     |
|                   | Entertainment      |                   |             |                      | ts.arena               |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Sports             | Club House        | 80302       | \[8, 803, 80302\]    | entertainment.spor     |
|                   | Entertainment      |                   |             |                      | ts.club\_house         |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Bars               | \-                | 804         | \[8, 804\]           | entertainment.bars     |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Casual Dining      | \-                | 805         | \[8, 805\]           | entertainment.cas      |
|                   |                    |                   |             |                      | ual\_dining            |
|                   |                    |                   |             |                      |                        |
| Entertainment     | QSR                | \-                | 806         | \[8, 806\]           | entertainment.qsr      |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Hotels             | \-                | 807         | \[8, 807\]           | entertainment.hote     |
|                   |                    |                   |             |                      | ls                     |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Hotels             | Lobby             | 80701       | \[8, 807, 80701\]    | entertainment.hote     |
|                   |                    |                   |             |                      | ls.lobby               |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Hotels             | Elevator          | 80702       | \[8, 807, 80702\]    | entertainment.hote     |
|                   |                    |                   |             |                      | ls.elevator            |
|                   |                    |                   |             |                      |                        |
| Entertainment     | Golf Carts         | \-                | 808         | \[8, 808\]           | entertainment.golf     |
|                   |                    |                   |             |                      | \_carts                |
|                   |                    |                   |             |                      |                        |
| Government        | \-                 | \-                | 9           | \[9\]                | government             |
|                   |                    |                   |             |                      |                        |
| Government        | DMVs               | \-                | 901         | \[9, 901\]           | government.dmv         |
|                   |                    |                   |             |                      |                        |
| Government        | Military Bases     | \-                | 902         | \[9, 902\]           | government.militar     |
|                   |                    |                   |             |                      | y\_bases               |
|                   |                    |                   |             |                      |                        |
| Financial         | \-                 | \-                | 10          | \[10\]               | financial              |
|                   |                    |                   |             |                      |                        |
| Financial         | Banks              | \-                | 1001        | \[10, 1001\]         | financial.banks        |
|                   |                    |                   |             |                      |                        |
| Residential       | \-                 | \-                | 11          | \[11\]               | residential            |
| Residential       | Apartment          | \-                | 1101        | \[11, 1101\]         | residential.apartm     |
|                   | Buildings          |                   |             |                      | ent\_buildings         |
|                   |                    |                   |             |                      |                        |
| Residential       | Apartment          | Lobby             | 110101      | \[11, 1101, 110101\] | residential.apartm     |
|                   | Buildings          |                   |             |                      | ent\_buildings.lobb    |
|                   |                    |                   |             |                      | y                      |
|                   |                    |                   |             |                      |                        |
| Residential       | Apartment          | Elevator          | 110102      | \[11, 1101, 110102\] | residential.apartm     |
|                   | Buildings          |                   |             |                      | ent\_buildings.elev    |
|                   |                    |                   |             |                      | ator                   |

# Specification Expansion & Amendment Process

This specification, written by the contributing parties, is not exhaustive and amenable to changes based on feedback from new participants. However, due to the initial adoption between the contributing parties, the frequency of changes shall be maintained on a cadence that respects the level of effort required by currently-integrated parties. As such, versioning of this spec will occur. Additionally, this spec can be amended on a quarterly cadence between contributors and adopters from the buy-side or sell-side.

