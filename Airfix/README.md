# Airfix Catalogue

## About Airfix

Airfix is a historic British model kit manufacturer, founded in 1939, that became synonymous with plastic scale modeling. Originally starting with inflatable rubber toys, the company revolutionized the hobby industry in 1952 by producing the first plastic model kit sold in UK shops - a Ferguson tractor in 1:72 scale. Airfix became particularly renowned for their extensive range of aircraft model kits, especially World War II subjects, but also expanded into military vehicles, ships, figures, and dioramas. The brand's affordable kits and iconic striped packaging made scale modeling accessible to generations of enthusiasts, establishing Airfix as a household name in Britain and beyond. Despite financial difficulties over the decades, including several ownership changes, Airfix has survived and continues to produce model kits today under the ownership of Hornby Hobbies, maintaining its position as one of the most recognized names in plastic modeling.

## Steve Pietrobon Data

I was looking for just set of data and came across Steve's work at http://www.sworld.com.au/steven/models/

There are three elements

* [Airfix Kit List from 1949](/Airfix/Airfix_Kit_List_utf8.txt) by Richard Humm and Steven Pietrobon. This file has been copied and converted to UTF-8 on 08-Nov-2025, updates may appear on Steven's website
* [Airfix Kit List in Series Order](/Airfix/Airfix_kits_in_series_order_utf8.txt) by Richard Humm. This file has been copied and converted to UTF-8 on 08-Nov-2025, updates may appear on Steven's website
* Parity check digit calculator for Airfix catalogue codes. A Pascal program by Steven Pietrobon and binary to calculate the catalogue code checksum. I have renamed the programme, removed the binary and created a Python version of this code

## Modified Data Set

* [Airfix_Kit_List.xlsx](/Airfix/Airfix_Kit_List.xlsx) - a normalized and standardized version of the original file with filters in Excel format

    * Dates of issue are based on announcements in Airfix Magazine, advertisements, reviews in other magazines and occasionally box styles and kit numbers.
    * Last dates of availability are based on catalogues, but some kits did become scarce before leaving the catalogue while others remained in the shops for years after their deletion. 
    * Where a kit is noted as issued "in" a specific year, official availability was confined to that year.

* [Airfix_Kits_In_Series_Order.xlsx](/Airfix/Airfix_Kits_In_Series_Order.xlsx) - a normalized and standardized version of the original file with filters in Excel format

    * Code 1 is the Pattern Number used on Type 0 and Type 1 kits, and on those kits when reissued in Type 2 packaging. 
    * Code 2 is the Pattern Number used on Type 2 and Type 3 kits, and shown as the Catalogue Number on Type 4 boxes and bags. 
    * Code 3 is the Code Number shown on Type 4 to Type 7 packaging. 
    * Code 4 is an alternative Code Number shown on Type 5 and Type 6 boxes for Series 1 historical ships, aircraft and military vehicles, and any alternatives shown in 1970s Airfix catalogues. 
    * Code 5 is the number shown on Palitoy produced kits. Column 6 is the number shown on Humbrol produced kits. 
    * A question mark on its own indicates that the kit number is not known. 
    * A question mark following a kit number indicates that the kit number has not been confirmed as appearing on a kit box. 
    * An X following a kit number indicates that the kit was never produced with that number. 

## Data Quality

**Please validate the data is suitable for your use case before using - use at your own peril**

* I can't speak to the quality of the original files, although random sampling has showing it to be very accurate.
* The conversion process is mainly automated and so that may have also introduced errors 

    
## Credits

List compiled by Richard Humm and Steven Pietrobon, with acknowledgements to the pioneering work of Pat Lewarne, Brad Hansen and John W Burns. Thanks also to Mario Wens, Claus Wilker and Andy Mullen for checking the list and providing information.