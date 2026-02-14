# A01376306_A5.2

## Overview

This project implements a Python-based system that calculates total
sales revenue using two JSON files:

-   A price catalogue containing product names and prices.
-   A sales record containing products sold and their quantities.

The program validates data, handles errors gracefully, measures
execution time, and generates a formatted sales report both on screen
and in a text file.

------------------------------------------------------------------------

## Objective

The goal of this assignment is to:

-   Practice file handling in Python.
-   Implement JSON data parsing.
-   Apply defensive programming and error handling.
-   Follow static code analysis best practices (Pylint compliant).
-   Generate formatted execution reports.
-   Measure execution time.

------------------------------------------------------------------------

## Project Structure

A01376306_A5.2-main/

-   computeSales.py \# Main program
-   priceCatalogue.json \# Product price catalogue
-   salesRecord.json \# Sales data input
-   SalesResults.txt \# Generated output report
-   Static_Analysis.png \# Evidence of static code analysis
-   README.md \# Project documentation

------------------------------------------------------------------------

## Requirements

-   Python 3.8 or higher
-   Standard library modules used:
    -   sys
    -   json
    -   time

------------------------------------------------------------------------

## How to Run the Program

From the command line, navigate to the project directory and run:

python computeSales.py priceCatalogue.json salesRecord.json

Example:

python computeSales.py priceCatalogue.json salesRecord.json

------------------------------------------------------------------------

## Program Workflow

1.  Validates command-line arguments.
2.  Loads JSON files safely using structured exception handling.
3.  Builds a dictionary for fast product price lookup.
4.  Computes total sales cost.
5.  Detects and reports:
    -   Missing products in the catalogue.
    -   Invalid quantity values.
6.  Measures execution time.
7.  Generates a formatted execution report.
8.  Writes results to:
    -   Console output
    -   SalesResults.txt

------------------------------------------------------------------------

## Error Handling

The program handles:

-   File not found errors.
-   Invalid JSON format.
-   OS-related file access errors.
-   Invalid product quantities.
-   Missing products in the catalogue.

All detected issues are reported without stopping execution.

------------------------------------------------------------------------

## Output Format

The program generates a structured report including:

-   Catalogue file used
-   Sales record file used
-   Total items processed
-   Total cost calculated
-   Execution time
-   Issues encountered (if any)

------------------------------------------------------------------------

## Performance Considerations

-   Uses dictionary lookup for efficient price searching (O(1)).
-   Measures execution time using time module.
-   Processes records in a single pass.

------------------------------------------------------------------------

## Learning Outcomes

This project demonstrates:

-   Modular programming
-   Defensive coding techniques
-   JSON file manipulation
-   Command-line argument processing
-   Structured reporting
-   Clean and maintainable code design

------------------------------------------------------------------------

## Author

Jorge Santana\
Student ID: A01376306
