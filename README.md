In diablo 2 LOD and D2R weapons with the 'Grinding' prefix can be sold and bought back for a gold profit. This script assumes the user has such a weapon equipped and automates the purchase flow.


Steps to run

1 - Download MPOS or any other software that helps you located the relative coordinates of your cursor to determine the locations of the in-game Sell Button, the coordinates of where you will need to click to interact
with your equiped weapon, and the coordinates of where you will need to interact to buy the weapon back

2- Replace the coordinate variables in the script to align with the ones for your screen

3- In terminal, navigate to the path of the scrip and type "python d2pyautogui.py" and enjoy



NOTE- All modding/scripting projects like this need to be done on offline characters where the TOS is more lax to projects/learning.





****MOCK BUG REPORT**** 

[D2R][UI] Weapons with the ‘GRINDING’ prefix can be sold for more than their buyback price. 

 

****Steps to Reproduce****- 
1. Find and equip a weapon with the ‘GRINDING’ prefix
2.Swap to classic graphics  
3.Navigate to an in-game shop keeper 
4.Navigate to a ‘Weapons’ tab within the shop and ensure there is enough room for the Grinding weapon to appear after selling 
5.Left click the ‘Sell’ button to sell the equipped weapon (Only way this exploit occurs, right-clicking to sell does not) 
6- Observe the gold increase 


****Reproduction Rate****- 100% 

****Version**** – Production version x.xx 

****Additional details****- 
Not all grinding prefix items sell for more than their buyback price, but they all sell for a different amount than the tooltip would indicate. 
