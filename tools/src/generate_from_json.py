####################################
# File name: generate_from_json.py #
# Author: Eric Kubischta / Lucit   #
# Organization: OpenOOH            #
#                                  #
# This tool will test, validate    #
# Generate final schema docs       #
# Based on the json data           #
#                                  #
####################################

import click
import os
import json
import shutil

#
# Global Variables and Constants!
#

# Root key name of the taxonomy
openooh_venue_taxonomy_root_key = "openooh_venue_taxonomy"

# The following top level keys are required (openooh_venue_taxonomy.{key})
openooh_venue_taxonomyKeys = (
    "version", "repository", "organization", "status", "specification")

# The keys required in each category/child_category/grandchild_category
openooh_venue_taxonomyCategoryKeys = (
    "name", "description", "enumeration_id", "string_value")

# The filenames of the final spec that appear in the specification dir
# and are copied during the promote process
openooh_venue_taxonomySpecFiles = ("specification.json", "specification.md")

# The version we are building, t
# this is passed in by the --build-version parameter to the script
buildVersion = ""


# Decorators for the main command
# These specify the cli params
@click.command()
@click.option("-bv", "--build-version", prompt="Which Version to Build?")
@click.option("-p", "--promote", is_flag=True)
@click.option("-t", "--test-only", is_flag=True)
# Main command
def main(build_version: str, test_only: str, promote: str) -> None:

    # Set the global variable containing the build version we are working on
    global buildVersion
    buildVersion = build_version

    show_intro()

    if not run_tests():
        return

    if test_only:
        return

    run_build()

    if promote:
        if verify_status_is_accepted_before_promoting():
            promote_spec()

    # Script complete, show final output message

    click.echo('')
    click.echo('')
    click.echo('   **********      ')
    click.echo('')
    click.echo(
        '    Spec documents updated.  Commit your changes')
    click.echo('')
    click.echo('')

    return


def run_build():
    # Build the .md markup files
    build_spec_markup()

    #
    #
    # Note, put any additional build processes here.
    # If you want an xml file built, or a csv file built, do that here
    #
    #


def run_tests():
    # Run various tests on the specification docs
    # These tests ensure that the documents meet
    # the rules for this specification
    # additional tests and validations should be added
    # into this function
    #
    #
    # Note, Put any additional schema tests here!
    #   Write a function that returns either true/false
    #   and test for it's result here
    #

    if not verify_dir():
        click.echo('  Cannot continue')
        return False

    if not verify_spec_json_exists():
        click.echo('  Cannot continue')
        return False

    if not verify_spec_header_exists():
        click.echo('  Cannot continue')
        return False

    if not verify_json():
        click.echo('  Cannot continue')
        return False

    if not verify_json_keys():
        click.echo('  Cannot continue')
        return False

    if not verify_all_enumeration_ids_are_unique():
        click.echo('  Cannot continue')
        return False

    if not verify_json_version_matches_buildVersion():
        click.echo('  Cannot continue')
        return False

    return True


def verify_dir():
    # Verify that the correct version directory exists
    path = get_version_dir()

    click.echo(f"Verifying that the {buildVersion} dir exists")

    isdir = os.path.isdir(path)

    if isdir:
        echo_success(f"Directory {path} Exists")
        return True
    else:
        echo_fail(f"Directory  {path} does Not Exist")
        return False


def verify_spec_json_exists():
    # Verify that the json file exists in the correct dir
    filename = get_specification_json_file_path()

    click.echo(f"Verifying that json file exists")

    isfile = os.path.isfile(filename)

    if isfile:
        echo_success(f"json file Exists")
        return True
    else:
        echo_fail(f"{filename} does Not Exist")
        return False


def verify_spec_header_exists():
    # Verify that the header file exists in the correct dir
    filename = get_specification_header_file_path()

    click.echo(f"Verifying that header file exists")

    isfile = os.path.isfile(filename)

    if isfile:
        echo_success(f"header Exists")
        return True
    else:
        echo_fail(f"{filename} does Not Exist")
        return False


def verify_json():
    # Validate that the json file is valid json data
    click.echo(f"Validating json data")
    json = get_specification_json()
    echo_success(f"json data ok")
    return True


def verify_json_keys():
    # Ensure that all the expected keys and values exist within the json data
    click.echo(f"Validating json keys")
    json = get_specification_json()

    keysOk = True

    if openooh_venue_taxonomy_root_key in json:
        echo_success(f"{openooh_venue_taxonomy_root_key} key ok")
    else:
        echo_fail(f"Base key `{openooh_venue_taxonomy_root_key}` is missing")
        keysOk = False
        return False

    for key in openooh_venue_taxonomyKeys:
        if key in json[openooh_venue_taxonomy_root_key]:
            echo_success(f"{openooh_venue_taxonomy_root_key}.{key} ok")
        else:
            echo_fail(
                f"key `{openooh_venue_taxonomy_root_key}.{key}` is missing")
            keysOk = False

    if not keysOk:
        return False

    # Check Categories
    if "categories" in json[openooh_venue_taxonomy_root_key]["specification"]:
        echo_success(
            f"{openooh_venue_taxonomy_root_key}.specification.categories ok")
    else:
        echo_fail(
            f"key `{openooh_venue_taxonomy_root_key}.specification.categories` is missing")
        keysOk = False

    if not keysOk:
        return False

    for category in json[openooh_venue_taxonomy_root_key]["specification"]["categories"]:
        keysOk = validateCategory(category)

    if not keysOk:
        return False

    return keysOk


def validateCategory(category):

    keysOk = True

    for key in openooh_venue_taxonomyCategoryKeys:
        categoryName = ""

        if "name" in category:
            categoryName = category["name"]

        if key in category:
            echo_success(f"category {categoryName}.{key} ok")
        else:
            echo_fail(f"key `category {categoryName}.{key}` is missing")
            keysOk = False

    if "children" in category:
        for childCategory in category["children"]:
            keysOk = validateChildCategory(
                childCategory, category["enumeration_id"])

    return keysOk


def validateChildCategory(category, parentEnumerationId):

    keysOk = True

    categoryName = ""

    if "name" in category:
        categoryName = category["name"]

    if isinstance(parentEnumerationId, int):
        echo_success(f"    enumeration_id for {categoryName} is an integer")
    else:
        echo_fail(f"    enumeration_id for {categoryName} is NOT an integer")
        keysOk = False

    for key in openooh_venue_taxonomyCategoryKeys:

        if key in category:
            echo_success(f"    child category {categoryName}.{key} ok")
        else:
            echo_fail(
                f"    key `child category {categoryName}.{key}` is missing")
            keysOk = False

    # Validate the enumeration id
    # It must be between parent_id * 100 + 1, and parent_id*100+00
    minId = parentEnumerationId * 100 + 1
    maxId = parentEnumerationId * 100 + 99

    if not minId <= category["enumeration_id"] <= maxId:
        echo_fail(
            f"Enumation Id for {categoryName} must be between {minId} - {maxId} ")

    if "children" in category:
        for childCategory in category["children"]:
            keysOk = validateGrandChildCategory(
                childCategory, category["enumeration_id"])

    return keysOk


def validateGrandChildCategory(category, parentEnumerationId):

    keysOk = True

    categoryName = ""

    if "name" in category:
        categoryName = category["name"]

    if isinstance(parentEnumerationId, int):
        echo_success(f"    enumeration_id for {categoryName} is an integer")
    else:
        echo_fail(f"    enumeration_id for {categoryName} is NOT an integer")
        keysOk = False

    for key in openooh_venue_taxonomyCategoryKeys:

        if key in category:
            echo_success(
                f"        grandchild category {categoryName}.{key} ok")
        else:
            echo_fail(
                f"        key `grandchild category {categoryName}.{key}` is missing")
            keysOk = False

    # Validate the enumeration id
    # It must be between parent_id * 100 + 1, and parent_id*100+00
    minId = parentEnumerationId * 100 + 1
    maxId = parentEnumerationId * 100 + 99

    if not minId <= category["enumeration_id"] <= maxId:
        echo_fail(
            f"Enumation Id for {categoryName} must be between {minId} - {maxId} ")

    if "children" in category:
        echo_fail(f"Grandchildren cannot have children beneath them")
        keysOk = False

    return keysOk


def verify_all_enumeration_ids_are_unique():
    # This will loop through ALL enumeration_ids to check for duplicates
    click.echo("Validation of unique enumeration_ids")

    json = get_specification_json()

    idsList = []

    for category in json[openooh_venue_taxonomy_root_key]["specification"]["categories"]:
        idsList.append(category["enumeration_id"])
        if "children" in category:
            for childCategory in category["children"]:
                idsList.append(childCategory["enumeration_id"])
                if "children" in childCategory:
                    for grandchildCategory in childCategory["children"]:
                        idsList.append(grandchildCategory["enumeration_id"])

    if len(set(idsList)) == len(idsList):
        echo_success("enumeration_id list is unique")
        return True
    else:
        echo_fail(
            "enumeration_id list is not unique, there are duplicated ids in the spec")
        seen_set = set()
        duplicate_set = set(
            x for x in idsList if x in seen_set or seen_set.add(x))
        unique_set = seen_set - duplicate_set

        click.echo("Duplicates : ")
        print(*duplicate_set, sep="\n")
        return False


def verify_json_version_matches_buildVersion():
    # This is a doublecheck done before promoting a version
    json = get_specification_json()

    jsonVersion = json[openooh_venue_taxonomy_root_key]["version"]

    if jsonVersion == buildVersion:
        echo_success(f"Build version {buildVersion} matches json")
        return True
    else:
        echo_fail(
            f"Build version {buildVersion} does not match JSON version {jsonVersion}")
        return False


def verify_status_is_accepted_before_promoting():
    # This is a doublecheck done before promoting a version

    json = get_specification_json()

    jsonStatus = json[openooh_venue_taxonomy_root_key]["status"]

    if jsonStatus == "accepted":
        echo_success(f"Json status is accepted and is promotable")
        return True
    else:
        echo_fail(f"Cannot promote spec because json status is not set to accepted")
        return False


#
# Markup Builder Functions
#

def build_spec_markup():

    click.echo(f"Generating Spec Markup")

    markup = ""
    markup = markup + get_parent_markup()

    specHeaderFile = get_specification_header_file_path()

    with open(specHeaderFile, 'r') as file:
        specHeader = file.read()

    finalSpec = specHeader + "\n" + markup + "\n"

    specFile = get_specification_md_file_path()

    okToContinue = True

    if os.path.isfile(specFile):
        okToContinue = click.confirm(
            'The specification file exists, are you sure you want to continue?')

    if okToContinue:
        f = open(specFile, "w")
        f.write(finalSpec)
        f.close()
        echo_success("Spec Markup Written to {specFile}")

    echo_success("Spec Markup Complete")


def get_parent_markup():
    json = get_specification_json()

    markup = "## Parent Categories & IDs\n"
    markup = markup + "|Parent Category|Enumeration ID|String Value|\n"
    markup = markup + "|---|---|---|\n"

    for category in json[openooh_venue_taxonomy_root_key]["specification"]["categories"]:
        markup = markup + \
            f"|{category['name']}|{category['enumeration_id']}|{category['string_value']}|\n"

    markup = markup + "\n"

    markup = markup + "## Child Categories & IDs\n"

    for category in json[openooh_venue_taxonomy_root_key]["specification"]["categories"]:
        if "children" in category:
            markup = markup + f"### {category['name']}\n"
            markup = markup + get_child_markup(category)

    markup = markup + "## Grandchild Categories & IDs\n"

    for category in json[openooh_venue_taxonomy_root_key]["specification"]["categories"]:
        if "children" in category:
            for child in category["children"]:
                if "children" in child:
                    markup = markup + f"### {category['name']} : {child['name']}\n"
                    markup = markup + get_grandchild_markup(category)

    return markup


def get_child_markup(category):

    markup = ""

    markup = markup + "|Child Category|Category Definition|Enumeration ID|String Value|\n"
    markup = markup + "|---|---|---|---|\n"

    for category in category["children"]:
        markup = markup + \
            f"|{category['name']}|{category['description']}|{category['enumeration_id']}|{category['string_value']}|\n"

    markup = markup + "\n"

    return markup


def get_grandchild_markup(category):

    markup = ""

    markup = markup + "|Grandchild Category|Category Definition|Enumeration ID|String Value|\n"
    markup = markup + "|---|---|---|---|\n"

    for category in category["children"]:
        markup = markup + \
            f"|{category['name']}|{category['description']}|{category['enumeration_id']}|{category['string_value']}|\n"

    markup = markup + "\n"

    return markup


def promote_spec():
    # This function promots the current buildVersion to be the latest published version of the spec
    # It creates the files in the ./specification/ dir
    click.echo("Promoting {buildVersion} to current")

    for specFile in openooh_venue_taxonomySpecFiles:
        click.echo("Copying {specFile}")
        specFileSource = get_version_dir()+"/"+specFile
        specFileDest = get_specification_dir()+"/"+specFile
        shutil.copyfile(specFileSource, specFileDest)
        echo_success("Copied {specFile}")


def show_intro():
    click.echo('')
    click.echo('')
    click.echo('   **********      ')
    click.echo('')
    click.echo('  OpenOOH Documentation Generator')
    click.echo(f"  Generating for Version {buildVersion}")
    click.echo('')
    click.echo('   **********      ')
    click.echo('')
    click.echo('')


#
# Some helper functions
#

def echo_success(message: str) -> None:
    okString = click.style('  OK  ', fg='green')
    click.echo(f"{okString} : {message}")


def echo_fail(message: str) -> None:
    failString = click.style(' FAIL ', fg='red')
    click.echo(f"{failString} : {message}")


def get_specification_dir() -> str:
    path = os.path.dirname(os.path.realpath(__file__))+'/../../specification/'
    return path


def get_version_dir() -> str:
    path = get_specification_dir()+buildVersion
    return path


def get_specification_json_file_path():

    path = get_version_dir()
    filename = path+"/specification.json"

    return filename


def get_specification_header_file_path():

    path = get_version_dir()
    filename = path+"/specification.header.md"

    return filename


def get_specification_md_file_path():

    path = get_version_dir()
    filename = path+"/specification.md"

    return filename


def get_specification_json():

    filename = get_specification_json_file_path()

    with open(filename) as f:
        data = json.load(f)

    return data


main()
