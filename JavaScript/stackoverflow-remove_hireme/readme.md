This is a short script for getting rid of sidebar "HireMe" box at stackoverflow.com. This box just disrupt 
my attention and focus.

This hack require Coogle Chrome plugin - Custom JavaScript for websites. You can find the plugin at: 
https://chrome.google.com/webstore/detail/custom-javascript-for-web/poakhlngfciodnhlhhgnaaelnpjljija 

Installation:
1. Install Custom JavaScript for website Google Chrome plugin and run it.
2. Go to any StackOverflow webpage.
3. Click on plugin info and select external scripts jQuery 2.1.0 
4. Insert following code snippet: 

function init() {
     $('#hireme').remove();
     $('#dfp-tsb').remove();
     $('#featured-company-page').remove();
}
window.onload = init;

5. Save and reload the website.

Tadaaaa!
