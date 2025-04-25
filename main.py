import database_handler
import visual_handler

items = [("Apples",139.00,10.00,5.00,122.55,50.00,500,"APPLE","Tim Cook","0999666333"),
          ("Raspberry",139.00,10.00,5.00,122.55,50.00,500,"RASPBERRY PI","Eben Upton","0111222333"),
          ("Orange",139.00,10.00,5.00,122.55,50.00,500,"ORANGE PI","Zhao Yifan","0555666777"),
          ("Bannana",139.00,10.00,5.00,122.55,50.00,500,"BANNANA PI","U.N. Owen","0333444555"),
          ("Potato",139.00,10.00,5.00,122.55,50.00,500,"LE POTATO LIBRE","W.H. Onos","0777888999")] # DEBUG

orders = [("Apples",139.00,10.00,5.00,122.55,1,"Tom Bakes","1999666333"),
          ("Raspberry",139.00,10.00,5.00,122.55,1,"Nebe Downton","1111222333"),
          ("Orange",139.00,10.00,5.00,122.55,1,"Zhao Yistan","1555666777"),
          ("Bannana",139.00,10.00,5.00,122.55,1,"K.N. Owen","1333444555"),
          ("Potato",139.00,10.00,5.00,122.55,1,"W.E. Noe","1777888999")] # DEBUG

database_handler.enter_mysql()
database_handler.initialise_new_items(items) # DEBUG
database_handler.initialise_new_orders(orders) # DEBUG
visual_handler.run_GUI()