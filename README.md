# python-inventory-analytics

An easy-to-use inventory visualisation software with a stylish dashboard for critical data insights. Designed for small to medium-sized businesses or for personal inventory tracking.


> ⚠️ Note: Not compatible with Python 3.13 (due to an error with X11).

## Features

* *Stunning* GUI via ttkbootstrap
  
* Tracking of inventory via linking with CSV file
  
* MySQL database integration

* **(WIP)** Visualisation of trends using powerful optimised algorithms

* **(WIP)** Compute basic analytics (e.g., most sold items, restock alerts)
  

## Libraries Used

All libraries are installable via pip3:

* numpy: for numerical operations and lightweight data analysis
```
pip3 install numpy
```
* ttkbootstrap: for styling the Tkinter GUI
```
pip3 install ttkbootstrap
```
* mysql-connector-python: for MySQL database interaction
```
pip3 install mysql-connector-python
```

## Getting Started
1. [Clone the Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

2. [Install MySQL](https://dev.mysql.com/downloads/)

3. <details> <summary> Create Inventory and Orders Table </summary>
      <details> <summary> Via Spreadsheet </summary>
        <p>This is what the Inventory Table should look like </p>
         <i>⚠️ONLY FIRST ROW MUST BE EXACTLY THE SAME IN YOURS</i>
         <br>
        ![Example Table for inventory](https://github.com/user-attachments/assets/b3e597e2-bedd-462b-8862-c55f5aadcf51)
        <p>This is what the Orders Table should look like </p>
         <i>⚠️ONLY FIRST ROW MUST BE EXACTLY THE SAME IN YOURS</i>
        <br>
        ![Example Table for Orders](https://github.com/user-attachments/assets/5344be90-97ff-4142-8e22-fb244056f475)
    </details>  
  
    <details> <summary> Via CSV </summary>
        <p>This is what the Inventory File should look like </p>
         <i>⚠️ONLY FIRST LINE MUST BE EXACTLY THE SAME IN YOURS</i>
         <br>
        ![image](https://github.com/user-attachments/assets/80364fc8-bfb5-4ec6-9f1a-bad18f1cc443)
        <p>This is what the Orders File should look like </p>
         <i>⚠️ONLY FIRST LINE MUST BE EXACTLY THE SAME IN YOURS</i>
        <br>
        ![image](https://github.com/user-attachments/assets/36d0cad5-ba0e-452a-b5cb-94a3c6072f5d)
    </details>
  </details>

4. <details> <summary> Export As CSV </summary>
      <details> <summary> From Spreadsheet </summary>
        <b>(Images in WIP)</b>
    </details>  
  
    <details> <summary> From CSV </summary>
        Already in CSV format
    </details>
  </details>

5. <details> <summary> Set <inventory_table>.csv as inventory path in Home-View </summary>
      <b>(Image in WIP)</b>
   </details>

6. <details> <summary> Set <orders_table>.csv as orders path in Home-View </summary>
      <b>(Image in WIP)</b>
   </details>
   
7. <details> <summary> Press Import Database Button </summary>
      <b>(Image in WIP)</b>
   </details>

8. <details> <summary> Press Refresh Button </summary>
      <b>(Image in WIP)</b>
   </details>

9. <details> <summary> Click Modelling View Button to switch to Modelling-View  </summary>
      <b>(Image in WIP)</b>
   </details>

## How to Run

Simply run the main Python file from the directory of the python-inventory-analytics folder:

```
python3 main.py
```


## Project Status

This project is currently a Work in Progress. 


## Contributions

Contributions are closed as of this time. 

## License

MIT License — see LICENSE file for details.
