# Feup-CMO

This repository contains code developed for the practical projects of [CMO (Mobile Communications)](https://sigarra.up.pt/feup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=459504) class.

## Lab2
Python script to analyse the output generated (txt file) by the [Radio Mobile Application](http://www.ve2dbe.com/english1.html), regarding simulations made.

### Install required package
```
pip install matplotlib
```

### How to run

```
python3 analyzer.py <file_name> <plot_min_rx> <plot_max_rx> <plot_number_bins>
```


| Name | Description | 
| -------- | -------- |
| **file_name**     | Name of the file to be analysed. File **must** be inside the CoverageResults directory.|
| **plot_min_rx**     | Minimum Rx value to be displayed on the Rx analysis histogram |
| **plot_min_rx**     | Maximum Rx value to be displayed on the Rx analysis histogram |
| **plot_number_bins**     | Number of desired divisions or bars in the values of the Rx histogram |


### Add more reports for analysis
**Move / Copy** the generated report to the **CoverageResults** directory, and run the script with the report's file name.