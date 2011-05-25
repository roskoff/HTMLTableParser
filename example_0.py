#!/usr/bin/env python

from pprint import pprint
from HTMLTableParser import HTMLTableParser

# Create the parser
p = HTMLTableParser()

try:
    # Create some html data to feed in the parser
    myData = """
 
        <html>
        <body>
            <table id="pricingTable"> 
                <thead> 
                  <tr> 
                    <th class="rowHeader"> 
                       Server Sizes:
                    </th> 
                    <th> 
                       Linux&reg;<span style="font-size:70%; vertical-align: top;">***</span> 
                         <div class="subtitle">Hourly (Estimated Monthly)</div> 
                    </th> 
                    <th> 
                       Windows&reg;
                       <div class="subtitle">Hourly (Estimated Monthly)</div> 
                    </th> 
                  </tr> 
                </thead> 
                <tbody> 
                  <tr> 
                    <td class="rowHeader"> 
                      <strong>256</strong>MB RAM
                      <div class="subtitle"><strong>10</strong>GB Disk</div> 
                    </td> 
                    <td class="highlight"> 
                        <strong>$0.015/hr.</strong> 
                      <div class="subtitle">($10.95/mo.)*</div> 
                    </td> 
                    <td>&mdash;</td> 
                  </tr> 
                </tbody> 
             </table>

             <table width="100%" id="anotherPricingTable"> 
             <thead> 
               <tr> 
                 <th>Plan</th> 
                 <th>Monthly Cost</th> 
                 <th>Server RAM Hours</th> 
                 <th>Effective Hourly Cost</th> 
                 <th>Overage Rate*</th> 
                 <th>Effective Server Cost<br />(per 0.5 GB RAM)</th> 
               </tr> 
             </thead> 
             <tbody> 
               <tr> 
                 <td>Professional Cloud</td> 
                 <td>$199.00</td> 
                 <td>2500</td> 
                 <td>$0.08</td> 
                 <td>$0.09</td> 
                 <td>$29.90/mo</td> 
               </tr> 
               <tr> 
                 <td>Business Cloud</td> 
                 <td>$999.00</td> 
                 <td>14,500</td> 
                 <td>$0.07</td> 
                 <td>$0.08</td> 
                 <td>$25.55/mo</td> 
               </tr> 
               <tr> 
                 <td colspan="3">&nbsp;</td> 
                 <td colspan="3" style="text-align: center; padding-top:10px;"> 
                   <a href="www.python.org">Go to Python</a> 
                 </td> 
               </tr> 
            </tbody> 
        </table> 

        </body>
        </html>
        """

    # Parse the data
    p.feed(myData)

except Exception, e:
    print e

# Show results
pprint(p.tables)

