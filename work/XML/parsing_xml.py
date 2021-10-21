import xml.etree.ElementTree
root = xml.etree.ElementTree.fromstring("""<?xml version = "1.0"?>
                                            <store>
                                               <item category = "weapon"> 
                                                   <power>50</power>
                                                   <cost>30</cost>
                                               </item>
                                               <item category = "spell">
                                                   <power>80</power>
                                                   <cost>100</cost>
                                               </item>
                                           </store>""")
print(root.tag)
