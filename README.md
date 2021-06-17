# venue-taxonomy

The intention of this project is to standardize the list of venue types that represent
Digital-Out-of-Home (DOOH) advertising screens within a programmatic OpenRTB 2.5 context.

The systematization of DOOH venue types will allow for clearer targeting by media buying
platforms across a spectrum of available supply-side platforms offering DOOH inventory.

## Specification

Written Specification

* [v1.1 Specification](./specification/specification.md)
  * [v1.1 JSON](./specification/specification.json) 

Resources
* PlaceExchange has contributed a mapping between v1.0 and the [DMI Taxonomy](./DMI%20DOOH%20ID%20Mapping.csv)
* Lucit has contributed a [JSON version](./specification/specification.json) of the spec (which may become the formal reference in the future)

## Previous Specification Versions
* [v1.0 Specification](./specification/1.0/specification.md)

## Specification Working Group

* Aura Koljonen (Broadsign)
* Bruno Guerrero (Hivestack)
* [Christian Collins](https://github.com/christiancollins11) (Vistar)
* Connor Peltz (Broadsign)
* [Eric Kubischta](https://github.com/ericlucit) (Lucit)
* [Jasleen Kaur](https://github.com/jasleenk-viooh) (VIOOH)
* [Jason Shao](https://github.com/jayshao) (PlaceExchange)
* Joshua Berg (MediaMath)
* [M. Wasfi](https://github.com/mowasfi7) (Verizon)
* Matthew Mercuri (Samsung)
* [Nicholas Babb](https://github.com/ndbabb) (Adomni)
* Sweta Vasudevan (PlaceExchange)
* William Hartley-Booth (The Trade Desk)

## Adoption

| Platform | Status | Version | Notes |
| ----------- | ------ | ------- | ----- |
| Adomni | Evaluating | 1.0 |  |
| Broadsign | Production | 1.0 | Supports OpenOOH v1.0.0 as of 8/3/20 |
| CAASie | Production | 1.0 | Supports OpenOOH v1.0.0 as of 07/16/20 |
| Campsite | Production | 1.0 | Supports OpenOOH v1.0.0 as of 12/03/20 |
| Hivestack | Production | 1.0 | Supports OpenOOH v1.0.0 as of 3/01/21 |
| OutMoove | Production | 1.0 | Supports OpenOOH v1.0.0 as of 09/07/20 |
| Place Exchange | Production | 1.0 | Support both DMI v1.0 and OpenOOH v1.0.0 as of 9/14/20 |
| Verizon Media | Production | 1.0 | Supports OpenOOH v1.0.0 as of 10/1/20 |
| VIOOH | Evaluating | 1.0 |  |
| Vistar Media | Production | 1.0 | Supports OpenOOH v1.0.0 (parent/child levels only) as of 9/9/20

## Tools and Build Process

### Overview of the process

The `specification` exists as 2 files which contain the source of truth for the most current version of this specification
- `./specification/specification.json`
- `./specification/specification.md`

These 2 files MUST NOT be edited directly, however, they are built using the `--promote` process listed below

The process is generally

- Create a new version directory `x.y` with 2 files in it `specification.json` and `specification.header.md`
- Make all changes to those 2 files
- Test your version
- Build your version
- Promote your version

**Start a new version `x.y`**
To start a new version, take the following steps
- Create a directory `./specification/[x.y]`
- Copy the following `2` files from the current version into that directory :
  - `./specification/[previous_ver]/specification.json`
  - `./specification/[previous_ver]/specification.header.md`
- Edit `./specification/[x.y]/specification.json` and change the following
  - `version` to `x.y`
  - `status` to `draft`


**Making changes to a current version `x.y`**

In general, the following process will take place for working on the current version of the spec that is in `draft` status
- Edit the `./specification/[x.y]/specification.json` with spec changes
- Edit the description of the spec in `./specification/[x.y]/specification.header.md`
- Test the spec with `./tools/bin/build --test-only --build-version=x.y`
- Build the spec with `./tools/bin/build --build-version=x.y`

When ready to release
- Edit `./specification/[x.y]/specification.json` and change status to `accepted`
- Build the spec with `./tools/bin/build --build-version=x.y`
- Promote the spec with `./tools/bin/build --build-version=x.y --promote`



### build command reference

**--build-version=**

Specify the version of the spec that you wish to build.  This essentially selects the correct directory that contains the files you are building

```
  # Build version 1.1 of this specification.  Ensure that the directory `./specification/1.1/` exists and contains `specification.json` and `specification.header.md`
  ./tools/bin/build --build-version=1.1
```

**--test-only**

Specify `--test-only` to only run the tests against json data

```
  # Test version 1.1
  ./tools/bin/build --build-version=1.1 --test-only
```


**--promote**

When a version is ready to become the final promoted (Current) standard execute this command to create the final specification documents
```
  # Promote version 1.1 and creates `./specification/specification.json` and `./specification/specification.md`
  ./tools/bin/build --build-version=1.1 --promote
```


